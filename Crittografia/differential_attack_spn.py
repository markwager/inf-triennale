import random

SBOX = [
    0xE, 0x2, 0x1, 0x3,
    0xD, 0x9, 0x0, 0x6,
    0xF, 0x4, 0x5, 0xA,
    0x8, 0xC, 0x7, 0xB
]

INV = [SBOX.index(i) for i in range(16)]

PBOX = [
    1, 5, 9, 13,
    2, 6, 10, 14,
    3, 7, 11, 15,
    4, 8, 12, 16
]

DELTA_X = 0x9009
DELTA_U4 = 0x1100


# ============================================================
# FUNZIONI DELLA SPN
# ============================================================

def sostituisci(x, box):
    risultato = 0

    for i in range(4):
        nibble = (x >> (12 - 4 * i)) & 0xF
        risultato = (risultato << 4) | box[nibble]

    return risultato


def permuta(x):
    bit = [(x >> (15 - i)) & 1 for i in range(16)]
    risultato = 0

    for posizione in PBOX:
        risultato = (risultato << 1) | bit[posizione - 1]

    return risultato


def genera_chiavi(chiave):
    # Cinque sottochiavi di 16 bit, secondo l'Esempio 4.1
    return [
        (chiave >> (16 - 4 * r)) & 0xFFFF
        for r in range(5)
    ]


def ingresso_ultimo_round(x, chiave):
    # Restituisce u4, prima della S-box del quarto round
    K = genera_chiavi(chiave)
    stato = x

    for r in range(3):
        stato ^= K[r]
        stato = sostituisci(stato, SBOX)
        stato = permuta(stato)

    return stato ^ K[3]


def cifra(x, chiave):
    K = genera_chiavi(chiave)
    u4 = ingresso_ultimo_round(x, chiave)

    return sostituisci(u4, SBOX) ^ K[4]


# ============================================================
# (a) DIFFERENTIAL DISTRIBUTION TABLE
# ============================================================

DDT = [[0] * 16 for _ in range(16)]

for dx in range(16):
    for x in range(16):
        dy = SBOX[x] ^ SBOX[x ^ dx]
        DDT[dx][dy] += 1

print("=" * 60)
print("(a) DIFFERENTIAL DISTRIBUTION TABLE")
print("=" * 60)

print("dx\\dy  " + " ".join(f"{i:X}" for i in range(16)))

for dx, riga in enumerate(DDT):
    print(f"{dx:X}      " + " ".join(f"{v:2}" for v in riga))

print("\nOgni riga somma a 16:",
      all(sum(riga) == 16 for riga in DDT))

print("ND(9,1) =", DDT[9][1])
print("ND(1,C) =", DDT[1][12])


# ============================================================
# (b) DIFFERENTIAL TRAIL
# ============================================================

p1 = DDT[9][1] / 16
p2 = DDT[9][1] / 16
p3 = DDT[9][1] / 16
p4 = DDT[1][12] / 16

probabilita = p1 * p2 * p3 * p4

print("\n" + "=" * 60)
print("(b) DIFFERENTIAL TRAIL")
print("=" * 60)

print("Differenza iniziale:       0x9009")
print("Differenza in ingresso a u4: 0x1100")

print("\nTransizioni delle S-box attive:")
print("S1^1: 9 -> 1, probabilita =", p1)
print("S4^1: 9 -> 1, probabilita =", p2)
print("S4^2: 9 -> 1, probabilita =", p3)
print("S4^3: 1 -> C, probabilita =", p4)

print(f"\nProbabilita teorica: {probabilita:.8f}")
print(f"Valore atteso 27/2048: {27 / 2048:.8f}")

# Verifica sperimentale del trail
CHIAVE_TEST = 0x3A94D63F
random.seed(10)

prove = 20000
successi_trail = 0

for _ in range(prove):
    x = random.randrange(0x10000)
    x2 = x ^ DELTA_X

    u = ingresso_ultimo_round(x, CHIAVE_TEST)
    u2 = ingresso_ultimo_round(x2, CHIAVE_TEST)

    if (u ^ u2) == DELTA_U4:
        successi_trail += 1

print("Prove sperimentali:", prove)
print("Coppie con differenza finale 0x1100:", successi_trail)
print(
    "Probabilità differenziale osservata:",
    f"{successi_trail / prove:.5f}"
)
print("Probabilità del singolo trail:", f"{27 / 2048:.8f}")


# ============================================================
# (c) ATTACCO DIFFERENZIALE
# ============================================================

def attacco_differenziale(coppie):
    conteggi = [[0] * 16 for _ in range(16)]
    filtrate = 0

    for x, x2, y, y2 in coppie:

        # FILTRAGGIO DELL'ALGORITHM 4.3 ADATTATO:
        # i nibble 3 e 4 dei cifrati devono coincidere.
        if (y & 0x00FF) != (y2 & 0x00FF):
            continue

        filtrate += 1

        # Prova tutte le 256 candidate dei primi 8 bit di K5.
        for L1 in range(16):
            v1 = ((y >> 12) & 0xF) ^ L1
            v1_2 = ((y2 >> 12) & 0xF) ^ L1

            u1 = INV[v1]
            u1_2 = INV[v1_2]

            # Il primo nibble di u4 deve avere differenza 1.
            if (u1 ^ u1_2) != 0x1:
                continue

            for L2 in range(16):
                v2 = ((y >> 8) & 0xF) ^ L2
                v2_2 = ((y2 >> 8) & 0xF) ^ L2

                u2 = INV[v2]
                u2_2 = INV[v2_2]

                # Il secondo nibble di u4 deve avere differenza 1.
                if (u2 ^ u2_2) == 0x1:
                    conteggi[L1][L2] += 1

    # Ordina le candidate per conteggio decrescente.
    candidate = sorted(
        (
            (conteggi[a][b], a, b)
            for a in range(16)
            for b in range(16)
        ),
        reverse=True
    )

    return candidate, filtrate


# ============================================================
# (d) TEST SPERIMENTALE
# ============================================================

print("\n" + "=" * 60)
print("(c)-(d) ATTACCO E TEST SPERIMENTALE")
print("=" * 60)

K = genera_chiavi(CHIAVE_TEST)
chiave_reale = (K[4] >> 8) & 0xFF

print(f"Chiave del test: {CHIAVE_TEST:08X}")
print(f"Primi 8 bit reali di K5: {chiave_reale:02X}")

# Genera al massimo 200 testi in chiaro:
# ogni coppia usa x e x XOR 0x9009.
random.seed(3)
coppie = []

for _ in range(100):
    x = random.randrange(0x10000)
    x2 = x ^ DELTA_X

    y = cifra(x, CHIAVE_TEST)
    y2 = cifra(x2, CHIAVE_TEST)

    coppie.append((x, x2, y, y2))

for numero_testi in (100, 150, 200):
    numero_coppie = numero_testi // 2
    dati = coppie[:numero_coppie]

    candidate, filtrate = attacco_differenziale(dati)

    punteggio, L1, L2 = candidate[0]
    stimata = (L1 << 4) | L2

    secondo_punteggio = candidate[1][0]
    recupero_univoco = (
        stimata == chiave_reale
        and punteggio > secondo_punteggio
    )

    print(f"\nTest con {numero_testi} testi in chiaro")
    print("Coppie utilizzate:", len(dati))
    print("Coppie che superano il filtro:", filtrate)
    print(f"Sottochiave candidata: {stimata:02X}")
    print("Conteggio della migliore candidata:", punteggio)
    print("Conteggio della seconda candidata:", secondo_punteggio)
    print("Sottochiave reale:", f"{chiave_reale:02X}")
    print("Recupero corretto e univoco:", recupero_univoco)
