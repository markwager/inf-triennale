import random
from collections import Counter

# ==============================================================================
# COSTANTI E VARIABILI GLOBALI (CRITTOSISTEMA SPN E DIFFERENZIALE)
# ==============================================================================

SBOX = []
SBOX_INV = []

PERM = []
PERM_INV = []

NR = 4 

BLOCK_L = 4
BLOCK_M = 4
SBOX_NO = 16
GROUP_MASK = 0xF
SIZEOF_INT = 16
MSG_MASK = 0xFFFF

# ==============================================================================
# FUNZIONI PER AGGIORNAMENTO DINAMICO S-BOX E PERMUTAZIONE
# ==============================================================================

def update_globals(new_sbox, new_perm):
    global SBOX, SBOX_INV, PERM, PERM_INV
    SBOX = new_sbox
    SBOX_INV = [SBOX.index(i) for i in range(16)]
    PERM = new_perm
    PERM_INV = [0] * 17
    for i in range(1, 17):
        PERM_INV[PERM[i]] = i

def load_last_sbox() -> str:
    try:
        with open('last_sbox.txt', 'r', encoding='utf-8') as f: return f.read().strip()
    except FileNotFoundError:
        return ''

def save_sbox(sbox_str: str) -> None:
    with open('last_sbox.txt', 'w', encoding='utf-8') as f: f.write(sbox_str)

def get_sbox() -> list[int]:
    prompt = """\nInserisci la S-Box (16 numeri da 0 a 15 separati da spazio)
Altrimenti inserisci 'rnd' per generare una S-Box casuale
Oppure premi invio per utilizzare l'ultima S-Box\n> """
    
    show_sbox = False
    while True:
        sbox_str = input(prompt).strip()
        
        if sbox_str == '':
            show_sbox = True
            sbox_str = load_last_sbox()
            
        if sbox_str.lower() == 'rnd' or sbox_str == '':
            sbox_list = list(range(16))
            random.shuffle(sbox_list)
            sbox_str = " ".join(map(str, sbox_list))
            show_sbox = True
            
        try:
            sbox = [int(x.replace(',', '')) for x in sbox_str.split()]
            if len(sbox) != 16 or set(sbox) != set(range(16)):
                raise ValueError("Servono esattamente i numeri da 0 a 15 senza ripetizioni.")
            save_sbox(" ".join(map(str, sbox)))
            break
        except ValueError as e:
            print("Errore: " + str(e) + " Riprova.\n")
            
    if show_sbox:
        print("S-Box utilizzata: " + " ".join(map(str, sbox)))
        
    return sbox

def load_last_perm() -> str:
    try:
        with open('last_perm.txt', 'r', encoding='utf-8') as f: return f.read().strip()
    except FileNotFoundError:
        return ''

def save_perm(perm_str: str) -> None:
    with open('last_perm.txt', 'w', encoding='utf-8') as f: f.write(perm_str)

def get_perm() -> list[int]:
    prompt = """\nInserisci la Permutazione P-Box (16 numeri da 1 a 16 separati da spazio)
Altrimenti inserisci 'rnd' per generare una permutazione casuale
Oppure premi invio per utilizzare l'ultima permutazione\n> """
    
    show_perm = False
    while True:
        perm_str = input(prompt).strip()
        
        if perm_str == '':
            show_perm = True
            perm_str = load_last_perm()
            
        if perm_str.lower() == 'rnd' or perm_str == '':
            perm_list = list(range(1, 17))
            random.shuffle(perm_list)
            perm_str = " ".join(map(str, perm_list))
            show_perm = True
            
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
        print("Permutazione utilizzata: " + " ".join(map(str, perm_vals)))
        
    return perm

# ==============================================================================
# FUNZIONI CORE DEL CIFRARIO E I/O CHIAVE
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
    show_key = False
    while True:
        chiave_str = input(KEY_PROMPT).strip()
        if chiave_str == '':
            show_key = True
            chiave_str = load_last_key()
        if chiave_str.lower() == 'rnd' or chiave_str == '':
            chiave_str = "{:0>20X}".format(random.randint(0, 0xFFFFFFFFFFFFFFFFFFFF))
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
# STRUMENTI PER L'ATTACCO DINAMICO
# ==============================================================================

def mask_inv(mask: int) -> int:
    return ~mask & MSG_MASK

def zeroed_groups_mask(x: int) -> int:
    mask = 0
    group_mask = GROUP_MASK
    for _ in range(BLOCK_M):
        if x & group_mask == 0: mask |= group_mask
        group_mask <<= BLOCK_L
    return mask

def is_right_pair(y1: int, y2: int, zero_mask: int) -> bool:
    return ((y1 ^ y2) & zero_mask) == 0

def candidate_keys(mask: int):
    k = mask
    while k <= MSG_MASK:
        yield k & mask_inv(mask)
        k += 1
        k |= mask

def backtrack(y: int, sbox_inv: list[int], key: int):
    return sub(y ^ key, sbox_inv)

def apply_mask(guess: int, mask: int) -> str:
    guess_mask = (((guess >> i) & 1, (mask >> i) & 1) for i in range(SIZEOF_INT - 1, -1, -1))
    return ''.join('_' if m == 0 else '1' if g else '0' for g, m in guess_mask)

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
    print("\n--- PUNTO B: RICERCA AUTOMATICA DELLA MIGLIOR TRACCIA DIFFERENZIALE ---")
    print("Scansione di tutte le 65535 possibili differenze di input (x') in corso...")
    
    best_prob = 0.0
    best_x_prime = 0
    best_u4 = 0
    best_num_passive = 0
    best_numeratore = 0
    best_denominatore = 1

    for candidate_x in range(1, 0x10000):
        stato_corrente = candidate_x
        prob_totale = 1.0
        numeratore = 1
        denominatore = 1
        
        for round_num in range(1, 4):
            stato_dopo_sbox = 0
            for sbox_idx in range(4):
                shift = 12 - 4 * sbox_idx
                nibble_in = (stato_corrente >> shift) & 0xF
                
                if nibble_in != 0:
                    massimo = max(ddt[nibble_in])
                    if massimo == 0:
                        prob_totale = 0
                        break
                    
                    possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                    nibble_out = possibili_uscite[-1]
                    
                    stato_dopo_sbox |= (nibble_out << shift)
                    prob_totale *= (massimo / 16.0)
                    numeratore *= massimo
                    denominatore *= 16
                    
            if prob_totale == 0:
                break
                
            stato_corrente = permute(stato_dopo_sbox, PERM)
            
        if prob_totale > 0:
            num_passive = sum(1 for i in range(4) if ((stato_corrente >> (12 - 4*i)) & 0xF) == 0)
            
            if num_passive > 0:
                if prob_totale > best_prob or (prob_totale == best_prob and num_passive > best_num_passive):
                    best_prob = prob_totale
                    best_x_prime = candidate_x
                    best_u4 = stato_corrente
                    best_num_passive = num_passive
                    best_numeratore = numeratore
                    best_denominatore = denominatore

    if best_prob == 0:
        print("\nERRORE CRITICO: Nessuna traccia utile trovata. La S-Box o Permutazione scelta disperde")
        print("troppo il segnale e non lascia S-Box passive sfruttabili al 4° round.")
        return 0, 0, 0

    print(f"\n=> MIGLIOR INPUT TROVATO: x' = 0x{best_x_prime:04X} ({best_num_passive} S-Box passive garantite)")
    print("Ricostruzione del percorso vincente:")
    
    stato_corrente = best_x_prime
    for round_num in range(1, 4):
        print("\nRound " + str(round_num) + ":")
        stato_dopo_sbox = 0
        for sbox_idx in range(4):
            shift = 12 - 4 * sbox_idx
            nibble_in = (stato_corrente >> shift) & 0xF
            
            if nibble_in == 0:
                print("  S-box " + str(sbox_idx + 1) + ": PASSIVA (Input 0x0, Output 0x0)")
            else:
                massimo = max(ddt[nibble_in])
                possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                nibble_out = possibili_uscite[-1]
                casi = ddt[nibble_in][nibble_out]
                stato_dopo_sbox |= (nibble_out << shift)
                print("  S-box " + str(sbox_idx + 1) + ": ATTIVA (Input 0x" + format(nibble_in, "X") + 
                      ", Output 0x" + format(nibble_out, "X") + "), casi " + str(casi) + " su 16)")
        
        print("  Stato prima della permutazione: 0x" + format(stato_dopo_sbox, "04X"))
        stato_corrente = permute(stato_dopo_sbox, PERM)
        print("  Stato dopo la permutazione:     0x" + format(stato_corrente, "04X"))

    print("\nStato finale (differenza attesa u4): 0x" + format(best_u4, "04X"))
    print("Probabilita totale della traccia (R_p): " + str(best_numeratore) + " su " + str(best_denominatore) + " (ovvero " + str(best_prob) + ")")
    
    return best_prob, best_x_prime, best_u4

def punto_c_attacco(probabilita_traccia, x_prime, u4_atteso, chiavi):
    if probabilita_traccia == 0:
        print("\nAttacco annullato: impossibile procedere senza una traccia valida.")
        return

    print("\n--- PUNTO C/D: ATTACCO DIFFERENZIALE E ANALISI PROBABILISTICA ---")
    
    print(f"\nAnalisi dello stato finale atteso (u4 = 0x{u4_atteso:04X}):")
    for i in range(4):
        nibble = (u4_atteso >> (12 - 4 * i)) & 0xF
        stato = "ATTIVA" if nibble != 0 else "PASSIVA"
        print(f"  S-Box {i+1}: {stato} (Differenza in ingresso: 0x{nibble:X})")

    chiave_vera_k5 = chiavi[4]
    
    passive_sbox_msk = zeroed_groups_mask(u4_atteso)
    active_sbox_msk = mask_inv(passive_sbox_msk)
    masked_real_key = chiave_vera_k5 & active_sbox_msk
    
    n_tentativi = int(input("\nInserisci il numero di tentativi da eseguire (invio per default = 1): ") or '1')
    riepilogo_tentativi = []

    for tentativo in range(1, n_tentativi + 1):
        print("\n" + "=" * 50)
        print(f"--- TENTATIVO {tentativo} DI {n_tentativi} ---")
        print("=" * 50)

        target_filtrate = int(input(f"Inserisci le coppie GIA' FILTRATE (invio per default = 20): ") or '20')

        print(f"\nGenerazione casuale di tuple fino a ottenere {target_filtrate} coppie filtrate...")
        coppie_filtrate = []
        totale_generate = 0

        while len(coppie_filtrate) < target_filtrate:
            totale_generate += 1
            x = random.randrange(0x10000)
            x_star = x ^ x_prime
            y = encrypt(x, chiavi)
            y_star = encrypt(x_star, chiavi)

            if is_right_pair(y, y_star, passive_sbox_msk):
                coppie_filtrate.append((x, x_star, y, y_star))

        candidates = Counter()
        for (x, x_star, y, y_star) in coppie_filtrate:
            for k in candidate_keys(passive_sbox_msk):
                yu = backtrack(y, SBOX_INV, k)
                y_star_u = backtrack(y_star, SBOX_INV, k)
                
                if ((yu ^ y_star_u) & active_sbox_msk) == u4_atteso: 
                    candidates[k] += 1

        classifica = candidates.most_common()
        hits_chiave_vera = candidates.get(masked_real_key, 0)
        
        if not classifica:
            print("Nessun candidato trovato.")
            continue

        hits_vincitore = classifica[0][1]
        ex_aequo = [k for (k, h) in classifica if h == hits_vincitore]
        
        if hits_chiave_vera == hits_vincitore and len(ex_aequo) == 1:
            risultato = "Riuscito"
        elif masked_real_key in ex_aequo:
            risultato = "Parziale (Pari Merito)"
        else:
            risultato = "Fallito"

        hits_miglior_falso = max((h for (k, h) in classifica if k != masked_real_key), default=0)
        
        riepilogo_tentativi.append({
            'tentativo': tentativo,
            'filtrate': target_filtrate,
            'generate': totale_generate,
            'hits_vera': hits_chiave_vera,
            'hits_miglior_falso': hits_miglior_falso,
            'risultato': risultato
        })

        print(f"\n  Top 5 Candidati S-box attive di K^5 (Maschera {active_sbox_msk:0>16b}):")
        print("  Pos | Sottochiave      | Hits | P_emp su Filtrate | Nota")
        print("  " + "-" * 60)

        for rank, (k, h) in zip(range(1, 6), classifica):
            p_su_filtrate = h / float(target_filtrate)
            nota = " <-- VERA CHIAVE" if k == masked_real_key else ""
            print(f"  {rank:3d} | {apply_mask(k, active_sbox_msk)} | {h:4d} |     {p_su_filtrate * 100:6.2f}%       |{nota}")

    print("\n\n" + "=" * 85)
    print(f"  SUNTO FINALE COMPARATIVO DEI {n_tentativi} TENTATIVI")
    print("=" * 85)
    print(f"Vera sottochiave K^5 da trovare: {chiave_vera_k5:0>16b} (Valore filtrato: {apply_mask(masked_real_key, active_sbox_msk)})")
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
        print(f"    - Valutazione: L'attacco e' molto robusto con le {target_filtrate} coppie filtrate scelte.")
    elif avg_gap > 0:
        print(f"    - Valutazione: L'attacco ha un margine ristretto. Potrebbe essere utile aumentare le coppie filtrate.")
    else:
        print(f"    - Valutazione: L'attacco non isola stabilmente la chiave. Aumentare significativamente le coppie filtrate.")

def main():
    while True:
        print("\n==================================================")
        print("  CRITTOGRAFIA SPN - MENU PRINCIPALE")
        print("==================================================")
        print("1. Cifra un messaggio")
        print("2. Decifra un messaggio")
        print("3. Esegui Crittoanalisi (Attacco Dinamico SPN 3.0)")
        print("0. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "0":
            break
            
        elif scelta == "1":
            print("\n--- CONFIGURAZIONE PARAMETRI ---")
            sbox_corrente = get_sbox()
            perm_corrente = get_perm()
            update_globals(sbox_corrente, perm_corrente)
            chiavi = get_key()
            
            print("\n--- CIFRATURA ---")        
            messaggio = input("Messaggio in chiaro da cifrare: ")
            cifrati = encrypt_message(messaggio, chiavi)
            print("Cifrato Hex:", "".join(format(b, "04X") for b in cifrati))
            
        elif scelta == "2":
            print("\n--- CONFIGURAZIONE PARAMETRI ---")
            sbox_corrente = get_sbox()
            perm_corrente = get_perm()
            update_globals(sbox_corrente, perm_corrente)
            chiavi = get_key()
            
            print("\n--- DECIFRATURA ---")
            cifrato_str = input("Testo cifrato in hex: ").replace(" ", "").replace("\n", "")
            blocchi = [int(cifrato_str[i:i+4], 16) for i in range(0, len(cifrato_str), 4)]
            print("Messaggio decifrato:", decrypt_message(blocchi, chiavi))
            
        elif scelta == "3":
            print("\n--- CONFIGURAZIONE PARAMETRI ---")
            sbox_corrente = get_sbox()
            perm_corrente = get_perm()
            update_globals(sbox_corrente, perm_corrente)
            chiavi = get_key()
            
            tabella = punto_a_ddt()
            prob, x_diff, u4_final = punto_b_traccia(tabella)
            punto_c_attacco(prob, x_diff, u4_final, chiavi)
            
        else:
            print("Opzione non valida.")

if __name__ == "__main__":
    main()