import random

# COSTANTI E IMPOSTAZIONI BASE
SBOX = [0xE, 2, 1, 3, 0xD, 9, 0, 6, 0xF, 4, 5, 0xA, 8, 0xC, 7, 0xB]
SBOX_INV = [SBOX.index(i) for i in range(16)]

PERM = [None, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
PERM_INV = [0] * 17 
for i in range(1, 17):
    PERM_INV[PERM[i]] = i

NR = 4 

def sub(x, box):
    return sum(box[(x >> (4 * i)) & 0xF] << (4 * i) for i in range(4))

def permute(x, table):
    y = 0
    for i in range(1, 17):
        if (x >> (16 - i)) & 1:
            y |= 1 << (16 - table[i])
    return y

def encrypt(p, keys):
    x = p
    for r in range(NR - 1):
        x = permute(sub(x ^ keys[r], SBOX), PERM)
    x = sub(x ^ keys[NR - 1], SBOX) ^ keys[NR]
    return x

def decrypt(c, keys):
    x = sub(c ^ keys[NR], SBOX_INV) ^ keys[NR - 1]
    for r in range(NR - 2, -1, -1):
        x = sub(permute(x, PERM_INV), SBOX_INV) ^ keys[r]
    return x

def key_from_hex(text):
    t = text.strip().lower()
    if t.startswith("0x"):
        t = t[2:]
    t = t.replace(" ", "").replace("-", "").replace("_", "")
    if len(t) != 20:
        raise ValueError("Servono 20 cifre esadecimali (80 bit). Ne hai inserite: " + str(len(t)))
    try:
        k = int(t, 16)
    except ValueError:
        raise ValueError("La chiave puo contenere solo cifre 0-9 e lettere a-f.")
    return [(k >> (16 * (4 - i))) & 0xFFFF for i in range(5)]

def encrypt_message(msg, keys):
    b = msg.encode()
    if len(b) % 2: 
        b += b"\x00"
    return [encrypt((b[i] << 8) | b[i + 1], keys) for i in range(0, len(b), 2)]

def decrypt_message(blocks, keys):
    out = bytearray()
    for c in blocks:
        p = decrypt(c, keys)
        out += bytes([p >> 8, p & 0xFF])
    return out.rstrip(b"\x00").decode(errors="replace")


# CRITTOANALISI DIFFERENZIALE DINAMICA (CON BINARI E ESADECIMALI)

def punto_a_ddt():
    print("\n--- PUNTO A: CALCOLO DDT ---")
    ddt = [[0] * 16 for _ in range(16)]
    for dx in range(16):
        for x in range(16):
            dy = SBOX[x] ^ SBOX[x ^ dx]
            ddt[dx][dy] += 1
    
    intestazione_colonne = " ".join(format(i, "04b") for i in range(16))
    print("x'\\y'       | " + intestazione_colonne)
    print("-" * 85)
    for dx, riga in enumerate(ddt):
        valori = " ".join(format(v, "4d") for v in riga)
        print("  " + format(dx, "X") + " (" + format(dx, "04b") + ") | " + valori)
    return ddt


def punto_b_traccia(ddt):
    print("\n--- PUNTO B: CALCOLO DELLA TRACCIA DIFFERENZIALE ---")
    x_prime = 0x9009
    print("Input iniziale differenziale x primo: 0x" + format(x_prime, "04X") + " (" + format(x_prime, "016b") + ")")
    
    stato_corrente = x_prime
    prob_totale = 1.0
    numeratore_totale = 1
    denominatore_totale = 1
    
    for round_num in range(1, 4):
        print("\nRound " + str(round_num) + ":")
        stato_dopo_sbox = 0
        
        for sbox_idx in range(4):
            shift = 12 - 4 * sbox_idx
            nibble_in = (stato_corrente >> shift) & 0xF
            
            if nibble_in == 0:
                print("  S-box " + str(sbox_idx + 1) + ": PASSIVA (Input 0x0 (0000), Output 0x0 (0000))")
            else:
                massimo = max(ddt[nibble_in])
                possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                nibble_out = possibili_uscite[-1]
                casi = ddt[nibble_in][nibble_out]
                
                stato_dopo_sbox |= (nibble_out << shift)
                prob_totale *= (casi / 16.0)
                numeratore_totale *= casi
                denominatore_totale *= 16
                
                print("  S-box " + str(sbox_idx + 1) + ": ATTIVA (Input 0x" + format(nibble_in, "X") + " (" + format(nibble_in, "04b") + ")" + 
                      ", Output 0x" + format(nibble_out, "X") + " (" + format(nibble_out, "04b") + "), casi " + str(casi) + " su 16)")
        
        print("  Stato intermedio prima della permutazione: 0x" + format(stato_dopo_sbox, "04X") + " (" + format(stato_dopo_sbox, "016b") + ")")
        stato_corrente = permute(stato_dopo_sbox, PERM)
        print("  Stato intermedio dopo la permutazione: 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
        
    print("\nStato finale (differenza in ingresso all'ultimo round): 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
    print("Probabilita totale della traccia (R_p): " + str(numeratore_totale) + " su " + str(denominatore_totale) + " (ovvero " + str(prob_totale) + ")")
    
    return prob_totale


def punto_c_attacco(probabilita_traccia):
    print("\n--- PUNTO C: ATTACCO DIFFERENZIALE ---")
    chiave_str = input("Inserisci una chiave maestra a 80 bit per simulare l'attacco (es. 0x1234567890ABCDEF1234): ")
    try:
        chiavi = key_from_hex(chiave_str)
    except ValueError as e:
        print("Errore: " + str(e))
        return

    C_COSTANTE = 6
    numero_coppie = int(C_COSTANTE * (1.0 / probabilita_traccia))
    
    print("Costante c scelta: " + str(C_COSTANTE))
    print("Calcolo coppie teoriche (T = c * 1/R_p): " + str(C_COSTANTE) + " * (1 / " + str(probabilita_traccia) + ") = " + str(numero_coppie))
    print("Generazione interna di " + str(numero_coppie) + " coppie di testi in chiaro con differenza 0x9009 (1001000000001001)...")
    
    coppie = []
    for i in range(numero_coppie):
        x = random.randrange(0x10000)
        x_star = x ^ 0x9009
        y = encrypt(x, chiavi)
        y_star = encrypt(x_star, chiavi)
        coppie.append((x, x_star, y, y_star))
        
    conteggi = [[0] * 16 for j in range(16)]
    filtrate = 0

    for (x, x_star, y, y_star) in coppie:
        if (y & 0x00FF) != (y_star & 0x00FF):
            continue
        filtrate += 1

        y1 = (y >> 12) & 0xF
        y1_star = (y_star >> 12) & 0xF
        y2 = (y >> 8) & 0xF
        y2_star = (y_star >> 8) & 0xF

        for L1 in range(16):
            u4_1_diff = SBOX_INV[y1 ^ L1] ^ SBOX_INV[y1_star ^ L1]
            if u4_1_diff == 0x1:
                for L2 in range(16):
                    u4_2_diff = SBOX_INV[y2 ^ L2] ^ SBOX_INV[y2_star ^ L2]
                    if u4_2_diff == 0x1:
                        conteggi[L1][L2] += 1

    classifica = sorted(
        ((conteggi[l1][l2], l1, l2) for l1 in range(16) for l2 in range(16)),
        reverse=True
    )
    
    hits, l1, l2 = classifica[0]
    sottochiave_trovata = (l1 << 4) | l2
    print("Coppie totali testate: " + str(numero_coppie) + " (sopravvissute al filtro: " + str(filtrate) + ")")
    print("La sottochiave vincente per i primi 8 bit di K^5 e 0x" + format(sottochiave_trovata, "02X") + 
          " (" + format(sottochiave_trovata, "08b") + ") con " + str(hits) + " hit")
    
    chiave_vera_k5 = chiavi[4]
    veri_8bit = (chiave_vera_k5 >> 8) & 0xFF
    print("Confronto: i veri 8 bit di K^5 inseriti sono 0x" + format(veri_8bit, "02X") + 
          " (" + format(veri_8bit, "08b") + ")")
    
    if sottochiave_trovata == veri_8bit:
        print("Risultato: Attacco Differenziale Riuscito.")
    else:
        print("Risultato: Attacco Fallito.")


# MENU INTERATTIVO PRINCIPALE

def main():
    while True:
        print("\n==================================================")
        print("  CRITTOGRAFIA SPN - MENU PRINCIPALE")
        print("==================================================")
        print("1. Cifra un messaggio")
        print("2. Decifra un messaggio")
        print("3. Esegui Crittoanalisi (Es. 4.16 - Punti a, b, c)")
        print("0. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "0":
            print("Chiusura del programma.")
            break
            
        elif scelta == "1":
            print("\n--- CIFRATURA ---")
            chiave_str = input("Inserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234): ")
            try:
                chiavi = key_from_hex(chiave_str)
                messaggio = input("Inserisci il messaggio in chiaro da cifrare: ")
                blocchi_cifrati = encrypt_message(messaggio, chiavi)
                esadecimale = "".join(format(b, "04X") for b in blocchi_cifrati)
                binario = "".join(format(b, "016b") for b in blocchi_cifrati)
                print("Messaggio cifrato in esadecimale: " + esadecimale)
                print("Messaggio cifrato in binario: " + binario)
            except ValueError as e:
                print("Errore: " + str(e))
                
        elif scelta == "2":
            print("\n--- DECIFRATURA ---")
            chiave_str = input("Inserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234): ")
            try:
                chiavi = key_from_hex(chiave_str)
                cifrato_str = input("Inserisci il testo cifrato in esadecimale: ")
                cifrato_str = cifrato_str.replace(" ", "").replace("\n", "")
                
                if len(cifrato_str) % 4 != 0:
                    print("Errore: La stringa esadecimale deve avere una lunghezza multipla di 4.")
                    continue
                    
                blocchi_cifrati = [int(cifrato_str[i:i+4], 16) for i in range(0, len(cifrato_str), 4)]
                binario = "".join(format(b, "016b") for b in blocchi_cifrati)
                print("Testo cifrato inserito in binario: " + binario)
                
                msg_decifrato = decrypt_message(blocchi_cifrati, chiavi)
                print("Messaggio decifrato: " + msg_decifrato)
            except ValueError as e:
                print("Errore: " + str(e))
                
        elif scelta == "3":
            tabella = punto_a_ddt()
            prob = punto_b_traccia(tabella)
            punto_c_attacco(prob)
            
        else:
            print("Opzione non valida. Riprova.")

main()