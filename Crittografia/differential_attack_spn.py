import os
import random

# ==============================================================================
# ARCHITETTURA SPN CON CHIAVE A 80 BIT (ESERCIZIO 4.16 STINSON)
# ==============================================================================

# S-box pi_S'' definita nell'Esercizio 4.16
SBOX = [
    0xE, 0x2, 0x1, 0x3,
    0xD, 0x9, 0x0, 0x6,
    0xF, 0x4, 0x5, 0xA,
    0x8, 0xC, 0x7, 0xB
]

# S-box inversa (pi_S'')^-1 calcolata automaticamente
INV_SBOX = [SBOX.index(i) for i in range(16)]

# Permutazione lineare pi_P (Example 4.1, indici 1..16)
PBOX = [
    1, 5, 9, 13,
    2, 6, 10, 14,
    3, 7, 11, 15,
    4, 8, 12, 16
]

# Differenziali della traccia dell'Esercizio 4.16
DELTA_X = 0x9009
DELTA_U4 = 0x1100


def sostituisci(stato_16bit, box):
    """Applica la S-box (o la sua inversa) ai 4 nibble di un blocco da 16 bit."""
    risultato = 0
    for i in range(4):
        nibble = (stato_16bit >> (12 - 4 * i)) & 0xF
        risultato = (risultato << 4) | box[nibble]
    return risultato


def permuta(stato_16bit):
    """Applica la permutazione lineare pi_P a un blocco da 16 bit."""
    bit = [(stato_16bit >> (15 - i)) & 1 for i in range(16)]
    risultato = 0
    for pos in PBOX:
        risultato = (risultato << 1) | bit[pos - 1]
    return risultato


def genera_sottochiavi_80bit(chiave_80bit):
    """
    Key Schedule a 80 bit:
    Prende una Master Key da 80 bit ed estrae 5 sottochiavi indipendenti
    da 16 bit ciascuna (K^1, K^2, K^3, K^4, K^5) senza finestra mobile.
    """
    return [
        (chiave_80bit >> (64 - 16 * r)) & 0xFFFF
        for r in range(5)
    ]


def ingresso_ultimo_round_80bit(x, chiave_80bit):
    """Calcola lo stato intermedio u^4 (ingresso alle S-box del Round 4)."""
    K = genera_sottochiavi_80bit(chiave_80bit)
    w = x
    for r in range(3):
        u = w ^ K[r]
        v = sostituisci(u, SBOX)
        w = permuta(v)
    return w ^ K[3]


def spn_encrypt_80bit(x, chiave_80bit):
    """Cifra un blocco da 16 bit usando una chiave maestra da 80 bit."""
    K = genera_sottochiavi_80bit(chiave_80bit)
    u4 = ingresso_ultimo_round_80bit(x, chiave_80bit)
    v4 = sostituisci(u4, SBOX)
    return v4 ^ K[4]


def spn_decrypt_80bit(y, chiave_80bit):
    """Decifra un blocco da 16 bit usando una chiave maestra da 80 bit."""
    K = genera_sottochiavi_80bit(chiave_80bit)
    v4 = y ^ K[4]
    u4 = sostituisci(v4, INV_SBOX)
    w = u4 ^ K[3]
    for r in range(2, -1, -1):
        v = permuta(w)
        u = sostituisci(v, INV_SBOX)
        w = u ^ K[r]
    return w


# ==============================================================================
# LETTURA DEI FILE DI INPUT (knownplaintext.txt E ciphertext.txt)
# ==============================================================================

def carica_knownplaintext(filename="knownplaintext.txt"):
    """
    Legge il file knownplaintext.txt strutturato come:
    x1,x2=y1,y2
    Restituisce una lista di tuple (x1, x2, y1, y2).
    """
    coppie = []
    if not os.path.exists(filename):
        raise FileNotFoundError("File " + filename + " non trovato nella cartella corrente.")

    with open(filename, "r", encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga or "=" not in riga:
                continue
            sx, dx = riga.split("=")
            x1_str, x2_str = sx.split(",")
            y1_str, y2_str = dx.split(",")
            coppie.append((
                int(x1_str.strip(), 16),
                int(x2_str.strip(), 16),
                int(y1_str.strip(), 16),
                int(y2_str.strip(), 16)
            ))
    return coppie


def carica_ciphertext(filename="ciphertext.txt"):
    """
    Legge il file ciphertext.txt e restituisce la lista dei blocchi
    cifrati da 16 bit (4 cifre esadecimali ciascuno).
    """
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        contenuto = f.read().strip().replace("\n", "").replace("\r", "").replace(" ", "")
    return [int(contenuto[i:i+4], 16) for i in range(0, len(contenuto), 4)]


# ==============================================================================
# PUNTO (a): CALCOLO DELLA TABELLA DEI VALORI N_D (DDT)
# ==============================================================================

def esegui_punto_a():
    print("=" * 72)
    print("(a) TABELLA DI DISTRIBUZIONE DELLE DIFFERENZE N_D (PER S-BOX pi_S'')")
    print("=" * 72)

    ddt = [[0] * 16 for _ in range(16)]
    for x_prime in range(16):
        for x in range(16):
            x_star = x ^ x_prime
            y_prime = SBOX[x] ^ SBOX[x_star]
            ddt[x_prime][y_prime] += 1

    header = "x'\\y' | " + " ".join(format(i, "2X") for i in range(16))
    print(header)
    print("-" * len(header))
    for x_prime, riga in enumerate(ddt):
        valori = " ".join(format(val, "2d") for val in riga)
        print("  " + format(x_prime, "X") + "   | " + valori)

    somma_16 = all(sum(r) == 16 for r in ddt)
    print("\nVerifica: tutte le righe sommano a 16: " + str(somma_16))
    print("Valori chiave per l'Es. 4.16: N_D(9, 1) = " + str(ddt[0x9][0x1]) +
          ", N_D(1, C) = " + str(ddt[0x1][0xC]))
    return ddt


# ==============================================================================
# PUNTO (b): TRACCIA DIFFERENZIALE CON R_p = 27/2048 (SU CHIAVE A 80 BIT)
# ==============================================================================

def esegui_punto_b(ddt):
    print("\n" + "=" * 72)
    print("(b) COSTRUZIONE DELLA TRACCIA DIFFERENZIALE (S^1_1, S^1_4, S^2_4, S^3_4)")
    print("=" * 72)

    # Rapporti di propagazione delle 4 S-box attive
    rp_s1_1 = ddt[0x9][0x1] / 16.0  # 6/16 = 3/8
    rp_s1_4 = ddt[0x9][0x1] / 16.0  # 6/16 = 3/8
    rp_s2_4 = ddt[0x9][0x1] / 16.0  # 6/16 = 3/8
    rp_s3_4 = ddt[0x1][0xC] / 16.0  # 4/16 = 1/4

    rp_totale = rp_s1_1 * rp_s1_4 * rp_s2_4 * rp_s3_4

    # Verifica programmatica della propagazione bit a bit nei 3 round
    u1_diff = DELTA_X                                # 0x9009
    v1_diff = (0x1 << 12) | 0x1                      # S^1_1: da 9 a 1, S^1_4: da 9 a 1 (0x1001)
    u2_diff = permuta(v1_diff)                       # P(0x1001) = 0x0009 (attiva S^2_4)
    v2_diff = 0x0001                                 # S^2_4: da 9 a 1 (0x0001)
    u3_diff = permuta(v2_diff)                       # P(0x0001) = 0x0001 (attiva S^3_4)
    v3_diff = 0x000C                                 # S^3_4: da 1 a C (0x000C)
    u4_diff = permuta(v3_diff)                       # P(0x000C) = 0x1100 (attiva S^4_1, S^4_2)

    print("Input Plaintext XOR (x') : 0x" + format(u1_diff, "04X") +
          " (bin: " + format(u1_diff, "016b") + ")")
    print("Round 1 (S^1_1, S^1_4)   : da u'^1 = 0x" + format(u1_diff, "04X") +
          " a v'^1 = 0x" + format(v1_diff, "04X") +
          " (R_p = " + str(rp_s1_1) + " * " + str(rp_s1_4) + " = 9/64)")
    print("Round 2 (S^2_4)          : da u'^2 = 0x" + format(u2_diff, "04X") +
          " a v'^2 = 0x" + format(v2_diff, "04X") +
          " (R_p = " + str(rp_s2_4) + " = 3/8)")
    print("Round 3 (S^3_4)          : da u'^3 = 0x" + format(u3_diff, "04X") +
          " a v'^3 = 0x" + format(v3_diff, "04X") +
          " (R_p = " + str(rp_s3_4) + " = 1/4)")
    print("Ingresso Round 4 (u'^4)  : u'^4 = 0x" + format(u4_diff, "04X") +
          " (bin: " + format(u4_diff, "016b") + ")")
    print("\nRapporto di propagazione teorico R_p = " + format(rp_totale, ".8f") +
          " (27/2048 = " + format(27 / 2048, ".8f") + ")")


# ==============================================================================
# PUNTO (c): ATTACCO DIFFERENZIALE SUL FILE knownplaintext.txt
# ==============================================================================

def attacco_differenziale_4_16(coppie):
    """
    Esegue l'Algorithm 4.3 adattato alla traccia dell'Esercizio 4.16 (u'^4 = 0x1100):
    - Filtraggio sulle S-box passive S^4_3 e S^4_4: gli ultimi 8 bit di y e y* devono coincidere.
    - Decifratura parziale sulle S-box attive S^4_1 e S^4_2 provando i 256 candidati (L1, L2)
      per i primi 8 bit della sottochiave finale K^5.
    """
    conteggi = [[0] * 16 for _ in range(16)]
    coppie_filtrate = 0

    for (x, x_star, y, y_star) in coppie:
        # Filtraggio: nibble 3 e nibble 4 devono avere differenza zero (0x00FF)
        if (y & 0x00FF) != (y_star & 0x00FF):
            continue

        coppie_filtrate += 1

        # Estrazione del 1° e 2° nibble dei testi cifrati (corrispondenti a S^4_1 e S^4_2)
        y1 = (y >> 12) & 0xF
        y1_star = (y_star >> 12) & 0xF

        y2 = (y >> 8) & 0xF
        y2_star = (y_star >> 8) & 0xF

        # Ciclo sulle 256 sottochiavi candidate (L1, L2) per (K^5_1, K^5_2)
        for L1 in range(16):
            v4_1 = y1 ^ L1
            v4_1_star = y1_star ^ L1
            u4_1_diff = INV_SBOX[v4_1] ^ INV_SBOX[v4_1_star]

            # Verifica differenza attesa u'^4_1 == 0x1
            if u4_1_diff == 0x1:
                for L2 in range(16):
                    v4_2 = y2 ^ L2
                    v4_2_star = y2_star ^ L2
                    u4_2_diff = INV_SBOX[v4_2] ^ INV_SBOX[v4_2_star]

                    # Verifica differenza attesa u'^4_2 == 0x1
                    if u4_2_diff == 0x1:
                        conteggi[L1][L2] += 1

    # Classifica decrescente di tutte le 256 combinazioni (conteggio, L1, L2)
    classifica = sorted(
        ((conteggi[l1][l2], l1, l2) for l1 in range(16) for l2 in range(16)),
        reverse=True
    )
    return classifica, coppie_filtrate


def esegui_punto_c(coppie_file):
    print("\n" + "=" * 72)
    print("(c) ATTACCO DIFFERENZIALE SULLE COPPIE DI 'knownplaintext.txt'")
    print("=" * 72)

    print("Totale coppie caricate da 'knownplaintext.txt': " + str(len(coppie_file)) +
          " (" + str(len(coppie_file) * 2) + " plaintexts)")
    xor_verifica = coppie_file[0][0] ^ coppie_file[0][1]
    print("Verifica XOR iniziale sulle coppie del file: 0x" + format(coppie_file[0][0], "04X") +
          " ^ 0x" + format(coppie_file[0][1], "04X") + " = 0x" + format(xor_verifica, "04X"))

    classifica, filtrate = attacco_differenziale_4_16(coppie_file)
    max_hits, best_L1, best_L2 = classifica[0]
    second_hits = classifica[1][0]

    print("Coppie che superano il filtro (y_3=y*_3 e y_4=y*_4): " +
          str(filtrate) + " su " + str(len(coppie_file)))
    print("\nTop 5 sottochiavi candidate (L1, L2) per i primi 8 bit di K^5:")
    for idx, (hits, l1, l2) in enumerate(classifica[:5], start=1):
        print("  " + str(idx) + ". (L1 = 0x" + format(l1, "X") + ", L2 = 0x" + format(l2, "X") +
              ") | Sottochiave Hex: 0x" + format(l1, "X") + format(l2, "X") +
              " (bin: " + format(l1, "04b") + " " + format(l2, "04b") + ") | Hit = " + str(hits))

    sottochiave_8bit = (best_L1 << 4) | best_L2
    print("\nSOTTOCHIAVE PARZIALE TROVATA (K^5_1, K^5_2): 0x" + format(sottochiave_8bit, "02X") +
          " (con " + str(max_hits) + " hit contro " + str(second_hits) + " della seconda)")
    return sottochiave_8bit


# ==============================================================================
# PUNTO (d): TEST SUL NUMERO DI PLAINTEXTS NECESSARI (100-200 PLAINTEXTS)
# ==============================================================================

def esegui_punto_d(coppie_file, target_subkey_8bit, blocchi_ciphertext):
    print("\n" + "=" * 72)
    print("(d) TEST SPERIMENTALE: QUANTI PLAINTEXTS SERVONO PER TROVARE LA CHIAVE?")
    print("=" * 72)
    print("Testiamo l'attacco su sottoinsiemi crescenti del file 'knownplaintext.txt'")
    print("(Nota: 1 coppia = 2 plaintexts; il libro stima circa 100-200 plaintexts):\n")

    print("  Plaintexts | Coppie (T) | Filtrate |  Top Key | 1 Hit  | 2 Hit  | Esito Recupero")
    print("-" * 78)

    # Testiamo da 50 plaintexts (25 coppie) fino a tutti i 1000 plaintexts (500 coppie)
    campioni_plaintexts = [50, 100, 120, 150, 180, 200, 300, 400, 600, 1000]

    for num_plaintexts in campioni_plaintexts:
        num_coppie = min(num_plaintexts // 2, len(coppie_file))
        sottoinsieme = coppie_file[:num_coppie]

        classifica, filtrate = attacco_differenziale_4_16(sottoinsieme)
        hits_1, l1, l2 = classifica[0]
        hits_2 = classifica[1][0]
        stimata = (l1 << 4) | l2

        univoca = (stimata == target_subkey_8bit) and (hits_1 > hits_2)
        if univoca:
            stato = "OK (Univoca)"
        elif stimata == target_subkey_8bit:
            stato = "Parimerito"
        else:
            stato = "Fallito"

        print(format(num_coppie * 2, "12d") + " | " +
              format(num_coppie, "10d") + " | " +
              format(filtrate, "8d") + " |     0x" +
              format(stimata, "02X") + " | " +
              format(hits_1, "6d") + " | " +
              format(hits_2, "6d") + " | " + stato)

    # Verifica architettura a 80 bit e lettura del file ciphertext.txt
    print("\n" + "=" * 72)
    print("VERIFICA ARCHITETTURA A 80 BIT E LETTURA 'ciphertext.txt'")
    print("=" * 72)
    if blocchi_ciphertext:
        print("File 'ciphertext.txt' letto correttamente: " + str(len(blocchi_ciphertext)) +
              " blocchi da 16 bit.")
        primi_blocchi = " ".join("0x" + format(b, "04X") for b in blocchi_ciphertext[:8])
        print("Primi 8 blocchi di 'ciphertext.txt': " + primi_blocchi)

        # Esempio di chiave a 80 bit (5 blocchi da 16 bit) che possiede 0x98 nei primi 8 bit di K^5
        k5_parziale = (target_subkey_8bit << 8) | 0x30
        chiave_80bit_esempio = (
            (0x1A2B << 64) |
            (0x3C4D << 48) |
            (0x5E6F << 32) |
            (0x7081 << 16) |
            k5_parziale
        )
        sottochiavi = genera_sottochiavi_80bit(chiave_80bit_esempio)
        print("Formato Chiave Maestra a 80 bit (20 hex): 0x" + format(chiave_80bit_esempio, "020X"))
        print("Sottochiavi da 16 bit estratte senza finestra mobile:")
        for idx, kr in enumerate(sottochiavi, start=1):
            print("    K^" + str(idx) + " = 0x" + format(kr, "04X") +
                  " (bin: " + format(kr, "016b") + ")")


# ==============================================================================
# ESECUZIONE DIRETTA DEL CODICE
# ==============================================================================

coppie_known = carica_knownplaintext("knownplaintext.txt")
blocchi_cipher = carica_ciphertext("ciphertext.txt")

tabella_ddt = esegui_punto_a()
esegui_punto_b(tabella_ddt)
sottochiave_trovata = esegui_punto_c(coppie_known)
esegui_punto_d(coppie_known, sottochiave_trovata, blocchi_cipher)