import random
from collections import Counter

# ==============================================================================
# COSTANTI E IMPOSTAZIONI BASE (CRITTOSISTEMA SPN E DIFFERENZIALE)
# ==============================================================================

SBOX = [0xE, 2, 1, 3, 0xD, 9, 0, 6, 0xF, 4, 5, 0xA, 8, 0xC, 7, 0xB]
SBOX_INV = [SBOX.index(i) for i in range(16)]

# PERM standard, ma l'algoritmo funzionerà con qualsiasi permutazione
PERM = [None, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
PERM_INV = [0] * 17 
for i in range(1, 17):
    PERM_INV[PERM[i]] = i

NR = 4 

# Costanti architetturali per l'attacco generico
BLOCK_L = 4
BLOCK_M = 4
SBOX_NO = 16
GROUP_MASK = 0xF
SIZEOF_INT = 16
MSG_MASK = 0xFFFF

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

KEY_PROMPT = """Inserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234)
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
    """Restituisce una maschera con bit a 1 in corrispondenza dei nibble nulli di x (S-box passive)."""
    mask = 0
    group_mask = GROUP_MASK
    for _ in range(BLOCK_M):
        if x & group_mask == 0: mask |= group_mask
        group_mask <<= BLOCK_L
    return mask

def is_right_pair(y1: int, y2: int, zero_mask: int) -> bool:
    return ((y1 ^ y2) & zero_mask) == 0

def candidate_keys(mask: int):
    """Genera tutti i candidati chiave possibili, forzando a 0 i bit dove la maschera è 1."""
    k = mask
    while k <= MSG_MASK:
        yield k & mask_inv(mask)
        k += 1
        k |= mask

def backtrack(y: int, sbox_inv: list[int], key: int):
    """Inverte parzialmente un ciphertext y attraverso la chiave k e l'ultimo strato di S-box."""
    return sub(y ^ key, sbox_inv)

def apply_mask(guess: int, mask: int) -> str:
    """Formatta la chiave indovinata mostrando '_' per i bit ignorati dalla maschera."""
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
                print("  S-box " + str(sbox_idx + 1) + ": ATTIVA (Input 0x" + format(nibble_in, "X") + 
                      ", Output 0x" + format(nibble_out, "X") + "), casi " + str(casi) + " su 16)")
        
        print("  Stato prima della permutazione: 0x" + format(stato_dopo_sbox, "04X"))
        stato_corrente = permute(stato_dopo_sbox, PERM)
        print("  Stato dopo la permutazione:     0x" + format(stato_corrente, "04X"))
        
    print("\nStato finale (differenza attesa u4): 0x" + format(stato_corrente, "04X"))
    print("Probabilita totale della traccia (R_p): " + str(numeratore_totale) + " su " + str(denominatore_totale) + " (ovvero " + str(prob_totale) + ")")
    return prob_totale, x_prime, stato_corrente

def punto_c_attacco(probabilita_traccia, x_prime, u4_atteso):
    print("\n--- PUNTO C/D: ATTACCO DIFFERENZIALE E ANALISI PROBABILISTICA ---")
    chiavi = get_key()
    chiave_vera_k5 = chiavi[4]
    
    # Derivazione dinamica delle maschere in base a u4_atteso
    passive_sbox_msk = zeroed_groups_mask(u4_atteso)
    active_sbox_msk = mask_inv(passive_sbox_msk)
    masked_real_key = chiave_vera_k5 & active_sbox_msk
    
    n_tentativi = int(input("Inserisci il numero di tentativi da eseguire (invio per default = 1): ") or '1')
    riepilogo_tentativi = []

    for tentativo in range(1, n_tentativi + 1):
        print("\n" + "=" * 50)
        print(f"--- TENTATIVO {tentativo} DI {n_tentativi} ---")
        print("=" * 50)

        c_costante = float(input(f"Inserisci la costante c (invio per default = 6): ") or '6.0')
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

            # Filtro dinamico: controlla le differenze sugli output dove ci aspettiamo 0
            if is_right_pair(y, y_star, passive_sbox_msk):
                coppie_filtrate.append((x, x_star, y, y_star))

        candidates = Counter()
        # Valutazione dinamica per tutti i candidati chiave permessi dalle S-Box attive
        for (x, x_star, y, y_star) in coppie_filtrate:
            for k in candidate_keys(passive_sbox_msk):
                yu = backtrack(y, SBOX_INV, k)
                y_star_u = backtrack(y_star, SBOX_INV, k)
                
                # Se la differenza parziale coincide con u4_atteso nelle S-Box attive
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
            'c': c_costante,
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
    print("-" * 85)
    print(" Tent. | c (teorico) | Filtrate | Generate | Hits Vera | Miglior Falso | Esito")
    print("-" * 85)
    for r in riepilogo_tentativi:
        print(f"  {r['tentativo']:3d}  |    {r['c']:6.2f}   |   {r['filtrate']:6d} |  {r['generate']:7d} |     {r['hits_vera']:3d}     |       {r['hits_miglior_falso']:3d}       | {r['risultato']}")
    print("-" * 85)

    successi = sum(1 for r in riepilogo_tentativi if r['risultato'] == "Riuscito")
    print(f"\n TASSO DI SUCCESSO GLOBALE: {successi}/{n_tentativi} ({(successi/n_tentativi)*100:.1f}%)")

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
            chiavi = get_key()
            messaggio = input("Messaggio in chiaro da cifrare: ")
            cifrati = encrypt_message(messaggio, chiavi)
            print("Cifrato Hex:", "".join(format(b, "04X") for b in cifrati))
        elif scelta == "2":
            chiavi = get_key()
            cifrato_str = input("Testo cifrato in hex: ").replace(" ", "").replace("\n", "")
            blocchi = [int(cifrato_str[i:i+4], 16) for i in range(0, len(cifrato_str), 4)]
            print("Messaggio decifrato:", decrypt_message(blocchi, chiavi))
        elif scelta == "3":
            tabella = punto_a_ddt()
            prob, x_diff, u4_final = punto_b_traccia(tabella)
            punto_c_attacco(prob, x_diff, u4_final)
        else:
            print("Opzione non valida.")

if __name__ == "__main__":
    main()