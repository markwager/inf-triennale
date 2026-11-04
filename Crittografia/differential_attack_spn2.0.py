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
# PERM = [None, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
PERM = [None, 8, 3, 15, 1, 12, 5, 11, 2, 16, 7, 4, 14, 9, 6, 13, 10]
# permutazione alternativa

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
# FUNZIONI INPUT CHIAVE
# ==============================================================================

KEY_PROMPT = """Inserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234)
Altrimenti inserisci 'rnd' per generare una chiave casuale
Oppure premi invio per utilizzare l'ultima chiave\n> """

def load_last_key() -> str:
    try:
        with open('last_key.txt', 'r', encoding='utf-8') as f: 
            input_key = f.read().strip()
    except FileNotFoundError:
        input_key = ''
    return input_key

def save_key(key: str) -> None:
    with open('last_key.txt', 'w', encoding='utf-8') as f: 
        f.write(key)

def get_key() -> list[int]:
    from random import randint
    
    show_key = False  # CORREZIONE: Inizializzazione necessaria per evitare UnboundLocalError
    
    while True:
        chiave_str = input(KEY_PROMPT).strip()
        
        if chiave_str == '':
            show_key = True
            chiave_str = load_last_key()
            
        # CORREZIONE: Controllo corretto per 'rnd' senza \n
        if chiave_str.lower() == 'rnd' or chiave_str == '':
            chiave_str = "{:0>20X}".format(randint(0, 0xFFFFFFFFFFFFFFFFFFFF))
            show_key = True
            
        try:
            chiavi = key_from_hex(chiave_str)
            save_key(chiave_str)
            break
        except ValueError as e:
            print("Errore: " + str(e) + " Riprova.\n")
            
    if show_key:
        print("Chiave utilizzata: 0x" + chiave_str.upper())
        
    return chiavi


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
                massimo = max(ddt[nibble_in]) # prende il valore Nd massimo sulla riga
                possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                # prende gli indici di colonna possibili perchè si potrebbe avere lo stesso valore massimo su più colonne
                nibble_out = possibili_uscite[-1] # ne prende uno tra questi indici, l'ultimo
                
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
    PUNTO C/D: Esegue n tentativi dell'attacco differenziale raccogliendo parametri, 
    stampa solo la classifica per ogni iterazione e termina con un riepilogo comparativo,
    concludendo con una stima delle coppie filtrate necessarie per la riuscita certa.
    """
    print("\n--- PUNTO C/D: ATTACCO DIFFERENZIALE E ANALISI PROBABILISTICA ---")
    
    # Estrazione dei differenziali attesi
    expected_u4_1 = (u4_atteso >> 12) & 0xF
    expected_u4_2 = (u4_atteso >> 8) & 0xF

    chiavi = get_key()

    chiave_vera_k5 = chiavi[4]
    veri_8bit = (chiave_vera_k5 >> 8) & 0xFF
    
    while True:
        input_tentativi = input("Inserisci il numero di tentativi da eseguire (invio per default = 1): ").strip()
        if input_tentativi == "":
            n_tentativi = 1
            break
        else:
            try:
                n_tentativi = int(input_tentativi)
                if n_tentativi <= 0:
                    print("Errore: il numero di tentativi deve essere > 0. Riprova.")
                else:
                    break
            except ValueError:
                print("Errore: inserisci un numero intero valido. Riprova.")

    riepilogo_tentativi = []

    for tentativo in range(1, n_tentativi + 1):
        print("\n==================================================")
        print(f"--- TENTATIVO {tentativo} DI {n_tentativi} ---")
        print("==================================================")

        while True:
            input_c = input(f"Inserisci la costante c per il tentativo {tentativo} (invio per default = 6): ").strip()
            if input_c == "":
                c_costante = 6.0
                break
            else:
                try:
                    c_costante = float(input_c)
                    if c_costante <= 0:
                        print("Errore: c deve essere > 0. Riprova.")
                    else:
                        break
                except ValueError:
                    print("Errore: inserisci un numero valido. Riprova.")

        inverso_rp = 1.0 / probabilita_traccia
        numero_coppie_teoriche = int(c_costante * inverso_rp)

        while True:
            input_filtrate = input(f"Inserisci le coppie GIA' FILTRATE per il tentativo {tentativo} (invio per default = 20): ").strip()
            if input_filtrate == "":
                target_filtrate = 20
                break
            else:
                try:
                    target_filtrate = int(input_filtrate)
                    if target_filtrate <= 0:
                        print("Errore: deve essere > 0. Riprova.")
                    else:
                        break
                except ValueError:
                    print("Errore: inserisci un intero valido. Riprova.")

        print(f"\nGenerazione casuale di tuple fino a ottenere {target_filtrate} coppie filtrate...")
        coppie_filtrate = []
        totale_generate = 0

        while len(coppie_filtrate) < target_filtrate:
            totale_generate += 1
            x = random.randrange(0x10000)
            x_star = x ^ x_prime
            y = encrypt(x, chiavi)
            y_star = encrypt(x_star, chiavi)

            if (y & 0x00FF) == (y_star & 0x00FF):
                coppie_filtrate.append((x, x_star, y, y_star))

        conteggi = [[0] * 16 for _ in range(16)]

        for (x, x_star, y, y_star) in coppie_filtrate:
            y1 = (y >> 12) & 0xF
            y1_star = (y_star >> 12) & 0xF
            y2 = (y >> 8) & 0xF
            y2_star = (y_star >> 8) & 0xF

            for L1 in range(16):
                u4_1_diff = SBOX_INV[y1 ^ L1] ^ SBOX_INV[y1_star ^ L1]
                if u4_1_diff == expected_u4_1:
                    for L2 in range(16):
                        u4_2_diff = SBOX_INV[y2 ^ L2] ^ SBOX_INV[y2_star ^ L2]
                        if u4_2_diff == expected_u4_2:
                            conteggi[L1][L2] += 1

        classifica = sorted(
            ((conteggi[l1][l2], l1, l2) for l1 in range(16) for l2 in range(16)),
            reverse=True
        )

        vero_l1 = (veri_8bit >> 4) & 0xF
        vero_l2 = veri_8bit & 0xF
        hits_chiave_vera = conteggi[vero_l1][vero_l2]

        hits_vincitore = classifica[0][0]
        ex_aequo = [((l1 << 4) | l2) for (h, l1, l2) in classifica if h == hits_vincitore]
        
        if hits_chiave_vera == hits_vincitore and len(ex_aequo) == 1:
            risultato = "Riuscito"
        elif veri_8bit in ex_aequo:
            risultato = "Parziale (Pari Merito)"
        else:
            risultato = "Fallito"

        # Trova il massimo punteggio ottenuto da una chiave SBAGLIATA
        hits_miglior_falso = max([h for (h, l1, l2) in classifica if ((l1 << 4) | l2) != veri_8bit] + [0])
        
        riepilogo_tentativi.append({
            'tentativo': tentativo,
            'c': c_costante,
            'filtrate': target_filtrate,
            'generate': totale_generate,
            'hits_vera': hits_chiave_vera,
            'hits_miglior_falso': hits_miglior_falso,
            'risultato': risultato
        })

        print("\n  Top 5 Candidati per i primi 8 bit di K^5 (L1, L2):")
        print("  Pos | Sottochiave | Hits | P_emp su Filtrate | Nota")
        print("  " + "-" * 60)

        for rank, (h, l1, l2) in enumerate(classifica[:5], start=1):
            cand_byte = (l1 << 4) | l2
            p_su_filtrate = h / float(target_filtrate)
            nota = " <-- VERA CHIAVE" if cand_byte == veri_8bit else ""
            print(f"  {rank:3d} | 0x{cand_byte:02X} ({cand_byte:08b}) | {h:4d} |     {p_su_filtrate * 100:6.2f}%       |{nota}")

    # =========================================================================
    # --- SUNTO FINALE COMPARATIVO E ANALISI QUALITATIVA ---
    # =========================================================================
    print("\n\n=====================================================================")
    print("  SUNTO FINALE COMPARATIVO DEI " + str(n_tentativi) + " TENTATIVI")
    print("=====================================================================")
    print(f"Vera sottochiave K^5 da trovare: 0x{veri_8bit:02X} ({veri_8bit:08b})")
    print("-" * 85)
    print(" Tent. | c (teorico) | Filtrate | Generate | Hits Vera | Miglior Falso | Esito")
    print("-" * 85)
    
    for r in riepilogo_tentativi:
        print(f"  {r['tentativo']:3d}  |    {r['c']:6.2f}   |   {r['filtrate']:6d} |  {r['generate']:7d} |     {r['hits_vera']:3d}     |       {r['hits_miglior_falso']:3d}       | {r['risultato']}")
    print("-" * 85)

    # Analisi Statistica Descrittiva
    successi = sum(1 for r in riepilogo_tentativi if r['risultato'] == "Riuscito")
    parziali = sum(1 for r in riepilogo_tentativi if r['risultato'] == "Parziale (Pari Merito)")
    fallimenti = sum(1 for r in riepilogo_tentativi if r['risultato'] == "Fallito")

    print("\n=====================================================================")
    print("  ANALISI QUALITATIVA E CONCLUSIONI CRITTOANALITICHE")
    print("=====================================================================")
    print(f" 1. TASSO DI SUCCESSO GLOBALE:")
    print(f"    - Successi Pieni:     {successi}/{n_tentativi} ({(successi/n_tentativi)*100:.1f}%)")
    print(f"    - Successi Parziali:  {parziali}/{n_tentativi} ({(parziali/n_tentativi)*100:.1f}%)")
    print(f"    - Fallimenti:         {fallimenti}/{n_tentativi} ({(fallimenti/n_tentativi)*100:.1f}%)")

    print(f"\n 2. METRICHE DI ISOLAMENTO DEL SEGNALE (Per Tentativo):")
    for r in riepilogo_tentativi:
        gap = r['hits_vera'] - r['hits_miglior_falso']
        
        print(f"    Tentativo {r['tentativo']} (Coppie Filtrate = {r['filtrate']}):")
        
        # Gap Analysis
        if gap > 0:
            print(f"      > Gap di vittoria: La chiave vera ha staccato i falsi candidati di {gap} hit(s).")
        elif gap == 0:
            print(f"      > Nessun Gap: La chiave vera e' confusa con il miglior falso positivo.")
        else:
            print(f"      > Gap negativo: Una chiave falsa ha superato la chiave vera di {abs(gap)} hit(s).")

    # =========================================================================
    # 3. CONSIDERAZIONE FINALE SUL NUMERO OTTIMALE DI COPPIE FILTRATE
    # =========================================================================
    tot_filtrate = sum(r['filtrate'] for r in riepilogo_tentativi)
    tot_generate = sum(r['generate'] for r in riepilogo_tentativi)
    tasso_filtro_medio = tot_filtrate / tot_generate if tot_generate > 0 else 0
    
    # Stinson suggerisce tipicamente c=6 per dominare il rumore statistico.
    c_sicurezza = 6.0
    t_consigliato = c_sicurezza / probabilita_traccia
    filtrate_consigliate = int(t_consigliato * tasso_filtro_medio)

    print(f"\n 3. CONSIDERAZIONE SUL NUMERO DI COPPIE NECESSARIE:")
    print(f"    La teoria della crittoanalisi differenziale indica che servono circa c=6")
    print(f"    'right pairs' per garantire un margine di vittoria netto sulla chiave vera.")
    print(f"    Per ottenere 6 right pairs, servirebbe generare T_teorico = 6 / R_p = {int(t_consigliato)} tuple casuali.")
    print(f"    Sulla base del tasso di filtraggio empirico medio osservato ({tasso_filtro_medio*100:.2f}%),")
    print(f"    il quantitativo stimato di COPPIE GIA' FILTRATE da richiedere in input")
    print(f"    per avere un attacco stabilmente 'Riuscito' e' di circa: {filtrate_consigliate} coppie (o superiore).")
            
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
        print("3. Esegui Crittoanalisi (Es. 4.16 - Punti a, b, c/d)")
        print("0. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "0":
            print("Chiusura del programma.")
            break
            
        elif scelta == "1":
            print("\n--- CIFRATURA ---")
            chiavi = get_key()
                    
            messaggio = input("Inserisci il messaggio in chiaro da cifrare: ")
            blocchi_cifrati = encrypt_message(messaggio, chiavi)
            esadecimale = "".join(format(b, "04X") for b in blocchi_cifrati)
            binario = "".join(format(b, "016b") for b in blocchi_cifrati)
            print("Messaggio cifrato in esadecimale: " + esadecimale)
            print("Messaggio cifrato in binario: " + binario)
                
        elif scelta == "2":
            print("\n--- DECIFRATURA ---")
            chiavi = get_key()
            
            while True:
                cifrato_str = input("Inserisci il testo cifrato in esadecimale: ")
                cifrato_str = cifrato_str.replace(" ", "").replace("\n", "")
                
                if len(cifrato_str) % 4 != 0:
                    print("Errore: La stringa esadecimale deve avere una lunghezza multipla di 4. Riprova.")
                    continue
                break
                
            try:
                blocchi_cifrati = [int(cifrato_str[i:i+4], 16) for i in range(0, len(cifrato_str), 4)]
                binario = "".join(format(b, "016b") for b in blocchi_cifrati)
                print("Testo cifrato inserito in binario: " + binario)
                
                msg_decifrato = decrypt_message(blocchi_cifrati, keys=chiavi)
                print("Messaggio decifrato: " + msg_decifrato)
            except ValueError as e:
                print("Errore in fase di decodifica: " + str(e))
                
        elif scelta == "3":
            tabella = punto_a_ddt()
            prob, x_diff, u4_final = punto_b_traccia(tabella)
            punto_c_attacco(prob, x_diff, u4_final)
            
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()