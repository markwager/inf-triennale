import random

# ==============================================================================
# COSTANTI E IMPOSTAZIONI BASE (CRITTOSISTEMA SPN)
# ==============================================================================

# SBOX: Permutazione fissa utilizzata nello strato di sostituzione.
# Mappa un input di 4 bit (indice da 0 a 15) in un output di 4 bit.
SBOX = [0xE, 2, 1, 3, 0xD, 9, 0, 6, 0xF, 4, 5, 0xA, 8, 0xC, 7, 0xB]

# SBOX_INV: Calcola automaticamente la S-box inversa per la decifratura.
# Trova l'indice 'i' in cui si trova il valore 'val', invertendo la mappatura.
SBOX_INV = [SBOX.index(i) for i in range(16)]

# PERM: Permutazione fissa dei 16 bit utilizzata nello strato di diffusione.
# Il valore all'indice 'i' (da 1 a 16) indica la nuova posizione del bit.
# L'indice 0 è riempito con 'None' per poter usare indici da 1 a 16 come in teoria.
PERM = [None, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

# PERM_INV: Calcola automaticamente la permutazione inversa.
PERM_INV = [0] * 17 
for i in range(1, 17):
    PERM_INV[PERM[i]] = i

# NR: Numero di round del cifrario SPN.
NR = 4 

# ==============================================================================
# FUNZIONI CORE DEL CIFRARIO
# ==============================================================================

def sub(x, box):
    """
    Applica lo strato di S-box a un blocco di 16 bit.
    Spezza i 16 bit in 4 nibble da 4 bit, passa ogni nibble nella S-box ('box')
    e ricompone il risultato shiftando i nibble nelle posizioni originali.
    """
    return sum(box[(x >> (4 * i)) & 0xF] << (4 * i) for i in range(4))

def permute(x, table):
    """
    Applica la permutazione dei bit (P-box) a un blocco di 16 bit 'x'.
    Legge ogni bit dalla posizione originale e lo posiziona secondo la tabella 'table'.
    """
    y = 0
    for i in range(1, 17):
        if (x >> (16 - i)) & 1:  # Se l'i-esimo bit di x (partendo da sinistra) è 1
            y |= 1 << (16 - table[i]) # Accende il bit corrispondente in y nella nuova posizione
    return y

def encrypt(p, keys):
    """
    Esegue la cifratura completa SPN su un blocco di plaintext 'p' (16 bit)
    utilizzando l'array di sottochiavi 'keys'.
    """
    x = p
    # Esegue i primi NR - 1 round standard (sostituzione + permutazione)
    for r in range(NR - 1):
        x = permute(sub(x ^ keys[r], SBOX), PERM)
    # L'ultimo round omette la permutazione finale e aggiunge il whitening
    x = sub(x ^ keys[NR - 1], SBOX) ^ keys[NR]
    return x

def decrypt(c, keys):
    """
    Esegue la decifratura completa SPN su un blocco di ciphertext 'c' (16 bit)
    eseguendo le operazioni inverse e scorrendo le sottochiavi a ritroso.
    """
    # Inverte l'ultimo round (rimozione whitening, S-box inversa, rimozione chiave round)
    x = sub(c ^ keys[NR], SBOX_INV) ^ keys[NR - 1]
    # Inverte i round precedenti (permutazione inversa, S-box inversa, rimozione chiave)
    for r in range(NR - 2, -1, -1):
        x = sub(permute(x, PERM_INV), SBOX_INV) ^ keys[r]
    return x

def key_from_hex(text):
    """
    Converte una stringa esadecimale (master key a 80 bit) in una lista di 5 sottochiavi
    da 16 bit ciascuna, estraendole in blocchi sequenziali.
    """
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
    # Estrae 5 blocchi da 16 bit partendo dai più significativi
    return [(k >> (16 * (4 - i))) & 0xFFFF for i in range(5)]

def encrypt_message(msg, keys):
    """
    Cifra un'intera stringa di testo dividendo i caratteri (convertiti in ASCII/bytes)
    in coppie per formare blocchi da 16 bit, aggiungendo padding se necessario.
    """
    b = msg.encode()
    if len(b) % 2: 
        b += b"\x00"
    return [encrypt((b[i] << 8) | b[i + 1], keys) for i in range(0, len(b), 2)]

def decrypt_message(blocks, keys):
    """
    Decifra una lista di blocchi cifrati a 16 bit e li ricompone in una stringa di testo.
    """
    out = bytearray()
    for c in blocks:
        p = decrypt(c, keys)
        out += bytes([p >> 8, p & 0xFF]) # Separa i due byte per ricostruire i caratteri
    return out.rstrip(b"\x00").decode(errors="replace")


# ==============================================================================
# FASE 2: CRITTOANALISI DIFFERENZIALE DINAMICA 
# ==============================================================================

def punto_a_ddt():
    """
    PUNTO A: Costruisce e stampa la Difference Distribution Table (DDT) per la S-box in uso.
    Restituisce la matrice DDT completa.
    """
    print("\n--- PUNTO A: CALCOLO DDT ---")
    
    # Inizializza la DDT come una matrice 16x16 riempita di zeri.
    # L'indice di riga è la differenza di input (x'), la colonna è la differenza di output (y').
    ddt = [[0] * 16 for _ in range(16)]
    
    # Itera su tutte le 16 possibili differenze di input (x')
    for dx in range(16): 
        # Itera su tutti i 16 possibili valori del testo in chiaro (x)
        for x in range(16): 
            # Calcola y': XOR tra l'uscita per x e l'uscita per x perturbato (x XOR x')
            dy = SBOX[x] ^ SBOX[x ^ dx] 
            # Incrementa il contatore per la transizione differenziale (x' -> y')
            ddt[dx][dy] += 1 
    
    # Stampa l'intestazione formattata della tabella in binario a 4 bit
    intestazione_colonne = " ".join(format(i, "04b") for i in range(16)) 
    print("x'\\y'       | " + intestazione_colonne) 
    print("-" * 85) 
    
    # Stampa i valori della DDT riga per riga
    for dx, riga in enumerate(ddt): 
        valori = " ".join(format(v, "4d") for v in riga) 
        print("  " + format(dx, "X") + " (" + format(dx, "04b") + ") | " + valori) 
        
    return ddt 


def punto_b_traccia(ddt):
    """
    PUNTO B: Traccia il percorso differenziale attraverso i primi 3 round del cifrario,
    identificando le S-box attive e passandone dinamicamente i valori attesi.
    """
    print("\n--- PUNTO B: CALCOLO DELLA TRACCIA DIFFERENZIALE ---")
    
    # Fissa il differenziale di input al cifrario (x' richiesto dall'esercizio 4.16)
    x_prime = 0x9009
    print("Input iniziale differenziale x primo: 0x" + format(x_prime, "04X") + " (" + format(x_prime, "016b") + ")")
    
    stato_corrente = x_prime
    prob_totale = 1.0
    numeratore_totale = 1
    denominatore_totale = 1
    
    # Itera attraverso i primi 3 round
    for round_num in range(1, 4):
        print("\nRound " + str(round_num) + ":")
        stato_dopo_sbox = 0
        
        # Analizza singolarmente le 4 S-box
        for sbox_idx in range(4):
            shift = 12 - 4 * sbox_idx
            # Estrae la differenza in ingresso al nibble corrente
            nibble_in = (stato_corrente >> shift) & 0xF
            
            # S-BOX PASSIVA (nessuna differenza in ingresso)
            if nibble_in == 0:
                print("  S-box " + str(sbox_idx + 1) + ": PASSIVA (Input 0x0 (0000), Output 0x0 (0000))")
            
            # S-BOX ATTIVA
            else:
                # Trova la transizione più probabile nella DDT per l'input corrente
                massimo = max(ddt[nibble_in])
                possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                # Prende l'output associato alla probabilità massima
                nibble_out = possibili_uscite[-1]
                
                # Numero di hit estratti dalla DDT
                casi = ddt[nibble_in][nibble_out]
                
                # Ricompone lo stato dopo la sostituzione
                stato_dopo_sbox |= (nibble_out << shift)
                
                # Aggiorna la probabilità cumulativa
                prob_totale *= (casi / 16.0)
                numeratore_totale *= casi
                denominatore_totale *= 16
                
                print("  S-box " + str(sbox_idx + 1) + ": ATTIVA (Input 0x" + format(nibble_in, "X") + " (" + format(nibble_in, "04b") + ")" + 
                      ", Output 0x" + format(nibble_out, "X") + " (" + format(nibble_out, "04b") + "), casi " + str(casi) + " su 16)")
        
        print("  Stato intermedio prima della permutazione: 0x" + format(stato_dopo_sbox, "04X") + " (" + format(stato_dopo_sbox, "016b") + ")")
        
        # Applica la permutazione di diffusione
        stato_corrente = permute(stato_dopo_sbox, PERM)
        print("  Stato intermedio dopo la permutazione: 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
        
    print("\nStato finale (differenza in ingresso all'ultimo round): 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
    print("Probabilita totale della traccia (R_p): " + str(numeratore_totale) + " su " + str(denominatore_totale) + " (ovvero " + str(prob_totale) + ")")
    
    # Ritorna i parametri necessari per eseguire l'attacco
    return prob_totale, x_prime, stato_corrente


def punto_c_attacco(probabilita_traccia, x_prime, u4_atteso):
    """
    PUNTO C: Esegue l'attacco differenziale decifrando parzialmente l'ultimo round
    e confrontando i differenziali calcolati con quelli estratti dinamicamente dalla traccia.
    """
    print("\n--- PUNTO C: ATTACCO DIFFERENZIALE ---")
    
    # ESTRAZIONE DINAMICA dei differenziali attesi per le S-box attive (nibble 1 e 2) dall'output del Round 3
    expected_u4_1 = (u4_atteso >> 12) & 0xF
    expected_u4_2 = (u4_atteso >> 8) & 0xF

    # Inserimento della chiave segreta maestra da attaccare
    chiave_str = input("Inserisci una chiave maestra a 80 bit per simulare l'attacco (es. 0x1234567890ABCDEF1234): ")
    try:
        chiavi = key_from_hex(chiave_str)
    except ValueError as e:
        print("Errore: " + str(e))
        return

    # Calcolo dinamico del numero di tuple necessarie (T = c / R_p)
    C_COSTANTE = 6
    numero_coppie = int(C_COSTANTE * (1.0 / probabilita_traccia))
    
    print("Costante c scelta: " + str(C_COSTANTE))
    print("Calcolo coppie teoriche (T = c * 1/R_p): " + str(C_COSTANTE) + " * (1 / " + str(probabilita_traccia) + ") = " + str(numero_coppie))
    print("Generazione interna di " + str(numero_coppie) + " tuple (x, x*, y, y*) con input differenziale 0x" + format(x_prime, "04X") + "...")
    
    coppie = []
    # Generazione dei campioni (Oracolo di cifratura simulato)
    for i in range(numero_coppie):
        x = random.randrange(0x10000)
        x_star = x ^ x_prime 
        y = encrypt(x, chiavi)
        y_star = encrypt(x_star, chiavi)
        coppie.append((x, x_star, y, y_star))
        
    # Inizializza la matrice dei contatori per i 256 candidati possibili dei primi 8 bit di K^5
    conteggi = [[0] * 16 for j in range(16)]
    filtrate = 0

    # Analisi di ogni tupla generata
    for (x, x_star, y, y_star) in coppie:
        
        # FASE DI FILTRAGGIO (S-box passive)
        # Controlla se gli ultimi 8 bit del ciphertext differiscono.
        # Se c'è una differenza, scarta la tupla poiché non segue la caratteristica prevista (right pair).
        if (y & 0x00FF) != (y_star & 0x00FF):
            continue
            
        filtrate += 1

        # Estrae i due nibble attivi in uscita per la decifratura parziale
        y1 = (y >> 12) & 0xF
        y1_star = (y_star >> 12) & 0xF
        y2 = (y >> 8) & 0xF
        y2_star = (y_star >> 8) & 0xF

        # FASE DI DECIFRATURA PARZIALE (Test dei 256 candidati per la sottochiave parziale K^5_1, K^5_2)
        for L1 in range(16):
            # Inverte whitening finale e strato di sostituzione, calcola la differenza
            u4_1_diff = SBOX_INV[y1 ^ L1] ^ SBOX_INV[y1_star ^ L1]
            
            # CONFRONTO DINAMICO con il differenziale atteso calcolato in punto_b
            if u4_1_diff == expected_u4_1: 
                for L2 in range(16):
                    u4_2_diff = SBOX_INV[y2 ^ L2] ^ SBOX_INV[y2_star ^ L2]
                    
                    if u4_2_diff == expected_u4_2: 
                        # Incrementa il contatore se entrambi i differenziali attesi convergono
                        conteggi[L1][L2] += 1

    # Appiattisce i conteggi e li ordina per numero di hit decrescenti
    classifica = sorted(
        ((conteggi[l1][l2], l1, l2) for l1 in range(16) for l2 in range(16)),
        reverse=True
    )
    
    # Prende il candidato con il conteggio massimo
    hits, l1, l2 = classifica[0]
    
    # Ricompone il byte vincente
    sottochiave_trovata = (l1 << 4) | l2
    
    print("Tuple totali testate: " + str(numero_coppie) + " (sopravvissute al filtro: " + str(filtrate) + ")")
    print("La sottochiave vincente per i primi 8 bit di K^5 e 0x" + format(sottochiave_trovata, "02X") + 
          " (" + format(sottochiave_trovata, "08b") + ") con " + str(hits) + " hit")
    
    # Verifica il successo dell'attacco confrontando con la vera sottochiave
    chiave_vera_k5 = chiavi[4]
    veri_8bit = (chiave_vera_k5 >> 8) & 0xFF
    
    print("Confronto: i veri 8 bit di K^5 inseriti sono 0x" + format(veri_8bit, "02X") + 
          " (" + format(veri_8bit, "08b") + ")")
    
    if sottochiave_trovata == veri_8bit:
        print("Risultato: Attacco Differenziale Riuscito.")
    else:
        print("Risultato: Attacco Fallito.")


# ==============================================================================
# MENU INTERATTIVO PRINCIPALE
# ==============================================================================

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
            prob, x_diff, u4_final = punto_b_traccia(tabella)
            punto_c_attacco(prob, x_diff, u4_final)
            
        else:
            print("Opzione non valida. Riprova.")

main()