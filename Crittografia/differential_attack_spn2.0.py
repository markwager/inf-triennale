import random

# ==============================================================================
# COSTANTI E IMPOSTAZIONI BASE (CRITTOSISTEMA SPN)
# ==============================================================================

SBOX = [0xE, 2, 1, 3, 0xD, 9, 0, 6, 0xF, 4, 5, 0xA, 8, 0xC, 7, 0xB]
SBOX_INV = [SBOX.index(i) for i in range(16)]

PERM = []
PERM_INV = []
NR = 4 

# ==============================================================================
# FUNZIONI PER AGGIORNAMENTO DINAMICO PERMUTAZIONE
# ==============================================================================

def update_globals_perm(new_perm):
    global PERM, PERM_INV
    PERM = new_perm
    PERM_INV = [0] * 17
    for i in range(1, 17):
        PERM_INV[PERM[i]] = i

def load_last_perm() -> str:
    try:
        with open('last_perm.txt', 'r', encoding='utf-8') as f: 
            return f.read().strip()
    except FileNotFoundError:
        return ''

def save_perm(perm_str: str) -> None:
    with open('last_perm.txt', 'w', encoding='utf-8') as f: 
        f.write(perm_str)

def get_perm() -> list[int]:
    prompt = """\nInserisci la Permutazione P-Box (16 numeri da 1 a 16 separati da spazio)
- Inserisci 'rnd' per generare una permutazione casuale
- Inserisci 'last' per caricare l'ultima permutazione salvata
- Premi INVIO per utilizzare la permutazione di DEFAULT (quella del libro)\n> """
    
    show_perm = False
    while True:
        perm_str = input(prompt).strip()
        
        if perm_str == '':
            perm_str = "1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16"
            show_perm = True
            print("=> Hai scelto la permutazione di DEFAULT del libro.")
            
        elif perm_str.lower() == 'last':
            loaded = load_last_perm()
            if not loaded:
                print("Errore: Nessuna permutazione salvata trovata in memoria. Riprova.")
                continue
            perm_str = loaded
            show_perm = True
            print("=> Hai scelto l'ULTIMA permutazione salvata.")
            
        elif perm_str.lower() == 'rnd':
            perm_list = list(range(1, 17))
            random.shuffle(perm_list)
            perm_str = " ".join(map(str, perm_list))
            show_perm = True
            print("=> Hai generato una permutazione CASUALE.")
            
        try:
            perm_vals = [int(x.replace(',', '')) for x in perm_str.split()]
            if len(perm_vals) != 16 or set(perm_vals) != set(range(1, 17)):
                raise ValueError("Servono esattamente i numeri da 1 a 16 senza ripetizioni.")
            save_perm(" ".join(map(str, perm_vals)))
            perm = [None] + perm_vals
            break
        except ValueError as e:
            print("Errore: " + str(e) + " Riprova.\n")
            
    if show_perm:
        print("Permutazione P-Box impostata: " + " ".join(map(str, perm_vals)))
        
    return perm

# ==============================================================================
# FUNZIONI CORE DEL CIFRARIO
# ==============================================================================

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
    if t.startswith("0x"): t = t[2:]
    t = t.replace(" ", "").replace("-", "").replace("_", "")
    if len(t) != 20: raise ValueError("Servono 20 cifre esadecimali (80 bit).")
    k = int(t, 16)
    return [(k >> (16 * (4 - i))) & 0xFFFF for i in range(5)]

def encrypt_message(msg, keys):
    b = msg.encode()
    if len(b) % 2: b += b"\x00"
    return [encrypt((b[i] << 8) | b[i + 1], keys) for i in range(0, len(b), 2)]

def decrypt_message(blocks, keys):
    out = bytearray()
    for c in blocks:
        p = decrypt(c, keys)
        out += bytes([p >> 8, p & 0xFF])
    return out.rstrip(b"\x00").decode(errors="replace")

# ==============================================================================
# FUNZIONI INPUT CHIAVE
# ==============================================================================

KEY_PROMPT = """\nInserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234)
Altrimenti inserisci 'rnd' per generare una chiave casuale
Oppure premi invio per utilizzare l'ultima chiave\n> """

def load_last_key() -> str:
    try:
        with open('last_key.txt', 'r', encoding='utf-8') as f: return f.read().strip()
    except FileNotFoundError:
        return ''

def save_key(key: str) -> None:
    with open('last_key.txt', 'w', encoding='utf-8') as f: f.write(key)

def get_key() -> list[int]:
    from random import randint
    show_key = False
    
    while True:
        chiave_str = input(KEY_PROMPT).strip()
        
        if chiave_str == '':
            show_key = True
            chiave_str = load_last_key()
            
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
    
    return prob_totale, x_prime, stato_corrente

def punto_c_attacco(probabilita_traccia, x_prime, u4_atteso):
    print("\n--- PUNTO C/D: ATTACCO DIFFERENZIALE E ANALISI PROBABILISTICA ---")
    
    print(f"\nAnalisi dello stato finale atteso (u4 = 0x{u4_atteso:04X}):")
    for i in range(4):
        nibble = (u4_atteso >> (12 - 4 * i)) & 0xF
        stato = "ATTIVA" if nibble != 0 else "PASSIVA"
        print(f"  S-Box {i+1}: {stato} (Differenza in ingresso: 0x{nibble:X})")
    
    expected_u4_1 = (u4_atteso >> 12) & 0xF
    expected_u4_2 = (u4_atteso >> 8) & 0xF

    chiavi = get_key()
    chiave_vera_k5 = chiavi[4]
    veri_8bit = (chiave_vera_k5 >> 8) & 0xFF
    
    while True:
        input_tentativi = input("\nInserisci il numero di tentativi da eseguire (invio per default = 1): ").strip()
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

        hits_miglior_falso = max([h for (h, l1, l2) in classifica if ((l1 << 4) | l2) != veri_8bit] + [0])
        
        riepilogo_tentativi.append({
            'tentativo': tentativo,
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
    print("-" * 75)
    print(" Tent. | Filtrate | Generate | Hits Vera | Miglior Falso | Esito")
    print("-" * 75)
    
    for r in riepilogo_tentativi:
        print(f"  {r['tentativo']:3d}  |   {r['filtrate']:6d} |  {r['generate']:7d} |     {r['hits_vera']:3d}     |       {r['hits_miglior_falso']:3d}       | {r['risultato']}")
    print("-" * 75)

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
        if gap > 0:
            print(f"      > Gap di vittoria: La chiave vera ha staccato i falsi candidati di {gap} hit(s).")
        elif gap == 0:
            print(f"      > Nessun Gap: La chiave vera e' confusa con il miglior falso positivo.")
        else:
            print(f"      > Gap negativo: Una chiave falsa ha superato la chiave vera di {abs(gap)} hit(s).")

    # =========================================================================
    # 3. EFFICIENZA DEL FILTRAGGIO E ROBUSTEZZA DELL'ATTACCO
    # =========================================================================
    tot_filtrate = sum(r['filtrate'] for r in riepilogo_tentativi)
    tot_generate = sum(r['generate'] for r in riepilogo_tentativi)
    tasso_filtro_medio = (tot_filtrate / tot_generate) * 100 if tot_generate > 0 else 0
    
    gaps = [r['hits_vera'] - r['hits_miglior_falso'] for r in riepilogo_tentativi]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0

    print(f"\n 3. EFFICIENZA DEL FILTRAGGIO E ROBUSTEZZA DELL'ATTACCO:")
    print(f"    - Efficienza setaccio: Il filtro scarta automaticamente circa il {100 - tasso_filtro_medio:.2f}%")
    print(f"      delle 'wrong pairs' (solo il {tasso_filtro_medio:.2f}% sopravvive per l'analisi).")
    print(f"    - Vantaggio medio della chiave vera: {avg_gap:.2f} hits rispetto al miglior falso positivo.")
    
    if avg_gap > 2:
        print(f"    - Valutazione: L'attacco e' molto robusto con le coppie filtrate scelte.")
    elif avg_gap > 0:
        print(f"    - Valutazione: L'attacco ha un margine ristretto. Potrebbe essere utile aumentare le coppie filtrate.")
    else:
        print(f"    - Valutazione: L'attacco non isola stabilmente la chiave. Aumentare significativamente le coppie filtrate.")
           
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
            print("\n--- CONFIGURAZIONE PARAMETRI ---")
            perm_corrente = get_perm()
            update_globals_perm(perm_corrente)
            
            print("\n--- CIFRATURA ---")
            chiavi = get_key()
                    
            messaggio = input("Inserisci il messaggio in chiaro da cifrare: ")
            blocchi_cifrati = encrypt_message(messaggio, chiavi)
            esadecimale = "".join(format(b, "04X") for b in blocchi_cifrati)
            binario = "".join(format(b, "016b") for b in blocchi_cifrati)
            print("Messaggio cifrato in esadecimale: " + esadecimale)
            print("Messaggio cifrato in binario: " + binario)
                
        elif scelta == "2":
            print("\n--- CONFIGURAZIONE PARAMETRI ---")
            perm_corrente = get_perm()
            update_globals_perm(perm_corrente)
            
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
            print("\n--- CONFIGURAZIONE PARAMETRI ---")
            perm_corrente = get_perm()
            update_globals_perm(perm_corrente)
            
            tabella = punto_a_ddt()
            prob, x_diff, u4_final = punto_b_traccia(tabella)
            punto_c_attacco(prob, x_diff, u4_final)
            
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()