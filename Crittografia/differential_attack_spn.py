
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
    
    # Inizializza la Difference Distribution Table (DDT) come una matrice 16x16 riempita di zeri.
    # L'indice di riga rappresenta la differenza di input (x'), l'indice di colonna la differenza di output (y').
    ddt = [[0] * 16 for _ in range(16)]
    
    # Itera su tutte le 16 possibili differenze di input (x'), da 0x0 a 0xF.
    for dx in range(16): 
        # Per una data differenza x', itera su tutti i 16 possibili valori del testo in chiaro x.
        for x in range(16): 
            # Calcola la differenza di output y' per la coppia (x, x*). 
            # x* è ottenuto come x XOR dx. La differenza y' è lo XOR delle rispettive uscite della S-box.
            dy = SBOX[x] ^ SBOX[x ^ dx] 
            
            # Incrementa di 1 il contatore nella cella corrispondente alla transizione (x' -> y').
            ddt[dx][dy] += 1 
    
    # Prepara la stringa di intestazione per le colonne della tabella, formattando i numeri da 0 a 15 in binario a 4 bit (es. '0000', '0001').
    intestazione_colonne = " ".join(format(i, "04b") for i in range(16)) 
    
    # Stampa la riga di intestazione principale della tabella.
    print("x'\\y'       | " + intestazione_colonne) 
    
    # Stampa una linea separatrice.
    print("-" * 85) 
    
    # Itera riga per riga la matrice DDT. 'dx' è l'indice della riga (x'), 'riga' è la lista dei 16 contatori per quella riga.
    for dx, riga in enumerate(ddt): 
        # Formatta ogni contatore 'v' della riga corrente in una stringa di 4 caratteri allineata a destra, per incolonnare bene i numeri.
        valori = " ".join(format(v, "4d") for v in riga) 
        
        # Stampa l'etichetta della riga (valore esadecimale e binario di x') seguita dai valori formattati dei contatori.
        print("  " + format(dx, "X") + " (" + format(dx, "04b") + ") | " + valori) 
        
    # Restituisce la matrice DDT completa per l'utilizzo nelle fasi successive dell'attacco.
    return ddt 


def punto_b_traccia(ddt):
    print("\n--- PUNTO B: CALCOLO DELLA TRACCIA DIFFERENZIALE ---")
    
    # Definisce la differenza di input iniziale per l'intero cifrario (x'), scelta in base all'esercizio.
    x_prime = 0x9009
    print("Input iniziale differenziale x primo: 0x" + format(x_prime, "04X") + " (" + format(x_prime, "016b") + ")")
    
    # Inizializza lo stato corrente della differenza con il valore di input x_prime.
    stato_corrente = x_prime
    
    # Inizializza le variabili per calcolare la probabilità complessiva della traccia differenziale.
    prob_totale = 1.0
    numeratore_totale = 1
    denominatore_totale = 1
    
    # Itera sui primi 3 round del cifrario per tracciare la propagazione della differenza.
    for round_num in range(1, 4):
        print("\nRound " + str(round_num) + ":")
        
        # Variabile per memorizzare la differenza dello stato dopo il passaggio attraverso lo strato di S-box.
        stato_dopo_sbox = 0
        
        # Itera sulle 4 S-box (da sinistra a destra).
        for sbox_idx in range(4):
            # Calcola l'ammontare di shift necessario per isolare il nibble (4 bit) in ingresso alla S-box corrente.
            shift = 12 - 4 * sbox_idx
            
            # Estrae la differenza in ingresso (nibble_in) per l'S-box corrente.
            nibble_in = (stato_corrente >> shift) & 0xF
            
            # Se la differenza in ingresso è 0, la S-box è considerata passiva e produrrà una differenza di uscita 0 con probabilità 1.
            if nibble_in == 0:
                print("  S-box " + str(sbox_idx + 1) + ": PASSIVA (Input 0x0 (0000), Output 0x0 (0000))")
            
            # Se la differenza in ingresso è diversa da 0, la S-box è attiva. Si deve determinare l'uscita più probabile.
            else:
                # Trova il valore massimo (il maggior numero di hit) nella riga della DDT corrispondente all'input 'nibble_in'.
                massimo = max(ddt[nibble_in])
                
                # Identifica tutti gli output (y') che presentano la massima probabilità (potrebbero essercene più di uno).
                possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                
                # Seleziona l'ultimo tra gli output più probabili come differenza in uscita (nibble_out) per questa S-box.
                nibble_out = possibili_uscite[-1]
                
                # Recupera il numero di hit dalla DDT per la transizione differenziale selezionata.
                casi = ddt[nibble_in][nibble_out]
                
                # Inserisce il nibble di output nella posizione corretta all'interno dello stato complessivo (stato_dopo_sbox).
                stato_dopo_sbox |= (nibble_out << shift)
                
                # Aggiorna la probabilità totale e i contatori frazionari moltiplicando per la probabilità della S-box corrente (casi/16).
                prob_totale *= (casi / 16.0)
                numeratore_totale *= casi
                denominatore_totale *= 16
                
                # Stampa i dettagli dell'attivazione della S-box, inclusi input, output e probabilità.
                print("  S-box " + str(sbox_idx + 1) + ": ATTIVA (Input 0x" + format(nibble_in, "X") + " (" + format(nibble_in, "04b") + ")" + 
                      ", Output 0x" + format(nibble_out, "X") + " (" + format(nibble_out, "04b") + "), casi " + str(casi) + " su 16)")
        
        # Stampa lo stato differenziale complessivo in uscita dallo strato delle S-box, prima della permutazione P.
        print("  Stato intermedio prima della permutazione: 0x" + format(stato_dopo_sbox, "04X") + " (" + format(stato_dopo_sbox, "016b") + ")")
        
        # Applica la permutazione (P-box) allo stato per rimescolare i bit della differenza. Questo diventa il nuovo stato corrente per il round successivo.
        stato_corrente = permute(stato_dopo_sbox, PERM)
        
        # Stampa lo stato differenziale dopo la permutazione.
        print("  Stato intermedio dopo la permutazione: 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
        
    # Al termine del ciclo, stampa la differenza prevista in ingresso al Round 4 (l'ultimo round attaccato).
    print("\nStato finale (differenza in ingresso all'ultimo round): 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
    
    # Stampa la probabilità globale della traccia, essenziale per determinare quante coppie di plaintext serviranno.
    print("Probabilita totale della traccia (R_p): " + str(numeratore_totale) + " su " + str(denominatore_totale) + " (ovvero " + str(prob_totale) + ")")
    
    # Restituisce la probabilità calcolata.
    return prob_totale


def punto_c_attacco(probabilita_traccia):
    print("\n--- PUNTO C: ATTACCO DIFFERENZIALE ---")
    
    # Richiede all'utente di inserire una chiave maestra da 80 bit in formato esadecimale per poter generare i cifrati da attaccare.
    chiave_str = input("Inserisci una chiave maestra a 80 bit per simulare l'attacco (es. 0x1234567890ABCDEF1234): ")
    try:
        # Tenta di convertire la stringa esadecimale fornita in una lista di sottochiavi per il cifrario.
        chiavi = key_from_hex(chiave_str)
    except ValueError as e:
        print("Errore: " + str(e))
        return

    # Imposta una costante (c = 6) che moltiplica l'inverso della probabilità della traccia per garantire un buon margine di successo statistico.
    C_COSTANTE = 6
    
    # Calcola il numero di coppie (x, x*) necessarie (T) utilizzando la formula T = c * (1 / R_p).
    numero_coppie = int(C_COSTANTE * (1.0 / probabilita_traccia))
    
    print("Costante c scelta: " + str(C_COSTANTE))
    print("Calcolo coppie teoriche (T = c * 1/R_p): " + str(C_COSTANTE) + " * (1 / " + str(probabilita_traccia) + ") = " + str(numero_coppie))
    print("Generazione interna di " + str(numero_coppie) + " coppie di testi in chiaro con differenza 0x9009 (1001000000001001)...")
    
    # Lista che conterrà le tuple complete generate: (x, x*, y, y*).
    coppie = []
    
    # Ciclo di generazione delle tuple.
    for i in range(numero_coppie):
        # Genera un plaintext x casuale a 16 bit.
        x = random.randrange(0x10000)
        
        # Crea il partner x* facendo lo XOR di x con la differenza di input iniziale stabilita (0x9009).
        x_star = x ^ 0x9009
        
        # Cifra x e x* usando la chiave fornita per simulare l'accesso a un oracolo di cifratura.
        y = encrypt(x, chiavi)
        y_star = encrypt(x_star, chiavi)
        
        # Aggiunge la tupla completa alla lista.
        coppie.append((x, x_star, y, y_star))
        
    # Inizializza una matrice 16x16 di contatori per tracciare quante volte ogni possibile combinazione dei due nibble bersaglio della sottochiave (L1, L2) soddisfa il differenziale atteso.
    conteggi = [[0] * 16 for j in range(16)]
    
    # Contatore per tenere traccia delle coppie che superano il processo di filtraggio.
    filtrate = 0

    # Itera su tutte le tuple generate.
    for (x, x_star, y, y_star) in coppie:
        
        # FASE DI FILTRAGGIO: Poiché la traccia prevede che le ultime due S-box del Round 4 siano passive, 
        # la differenza tra i cifrati finali negli ultimi 8 bit deve essere zero. 
        # Se (y AND 0x00FF) è diverso da (y_star AND 0x00FF), la coppia non segue la traccia ed è scartata immediatamente.
        if (y & 0x00FF) != (y_star & 0x00FF):
            continue
            
        # Incrementa il contatore delle coppie che sono sopravvissute al filtro.
        filtrate += 1

        # Isola i primi due nibble (4 bit ciascuno) di y e y*, che corrispondono agli input invertiti delle due S-box attive nel Round 4 (S1^4 e S2^4).
        y1 = (y >> 12) & 0xF
        y1_star = (y_star >> 12) & 0xF
        y2 = (y >> 8) & 0xF
        y2_star = (y_star >> 8) & 0xF

        # FASE DI DECIFRATURA PARZIALE E VERIFICA.
        # Itera su tutte le 16 possibili ipotesi (L1) per il primo nibble della sottochiave K^5.
        for L1 in range(16):
            
            # Esegue lo XOR tra i nibble cifrati e la candidata L1 (rimozione del whitening), 
            # poi applica l'inversa della S-box. Infine, calcola la differenza (XOR) tra i due input S-box ricostruiti (u^4_1).
            u4_1_diff = SBOX_INV[y1 ^ L1] ^ SBOX_INV[y1_star ^ L1]
            
            # Se la differenza ricostruita per la prima S-box (S1^4) coincide con il differenziale atteso dalla traccia (0x1), 
            # procede a testare il secondo nibble della sottochiave.
            if u4_1_diff == 0x1:
                
                # Itera su tutte le 16 possibili ipotesi (L2) per il secondo nibble della sottochiave K^5.
                for L2 in range(16):
                    
                    # Decifratura parziale e calcolo della differenza per il secondo blocco (u^4_2).
                    u4_2_diff = SBOX_INV[y2 ^ L2] ^ SBOX_INV[y2_star ^ L2]
                    
                    # Se anche la differenza per la seconda S-box (S2^4) coincide con il differenziale atteso (0x1),
                    # significa che l'ipotesi della sottochiave (L1, L2) è compatibile con questa specifica "right pair".
                    if u4_2_diff == 0x1:
                        # Incrementa il contatore per la candidata (L1, L2).
                        conteggi[L1][L2] += 1

    # Appiattisce la matrice dei conteggi in una lista di tuple (hit, L1, L2) e la ordina in ordine decrescente in base al numero di hit.
    classifica = sorted(
        ((conteggi[l1][l2], l1, l2) for l1 in range(16) for l2 in range(16)),
        reverse=True
    )
    
    # Estrae la candidata (L1, L2) che ha ottenuto il punteggio (hit) più alto, ovvero la più probabile.
    hits, l1, l2 = classifica[0]
    
    # Combina i due nibble L1 e L2 in un singolo byte (8 bit) per ottenere la porzione ricostruita della sottochiave K^5.
    sottochiave_trovata = (l1 << 4) | l2
    
    # Stampa le statistiche relative al processo di filtraggio e la sottochiave vincente.
    print("Coppie totali testate: " + str(numero_coppie) + " (sopravvissute al filtro: " + str(filtrate) + ")")
    print("La sottochiave vincente per i primi 8 bit di K^5 e 0x" + format(sottochiave_trovata, "02X") + 
          " (" + format(sottochiave_trovata, "08b") + ") con " + str(hits) + " hit")
    
    # Estrae i veri primi 8 bit della sottochiave finale K^5 (chiavi[4]) inserita inizialmente, per poter verificare se l'attacco ha avuto successo.
    chiave_vera_k5 = chiavi[4]
    veri_8bit = (chiave_vera_k5 >> 8) & 0xFF
    
    # Stampa i veri 8 bit per il confronto.
    print("Confronto: i veri 8 bit di K^5 inseriti sono 0x" + format(veri_8bit, "02X") + 
          " (" + format(veri_8bit, "08b") + ")")
    
    # Confronta la sottochiave trovata dall'attacco con quella vera e dichiara l'esito.
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
