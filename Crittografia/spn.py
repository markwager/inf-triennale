import random

# S-box
PI_S = [0xE, 0x2, 0x1, 0x3, 0xD, 0x9, 0x0, 0x6, 
        0xF, 0x4, 0x5, 0xA, 0x8, 0xC, 0x7, 0xB]

# Calcoliamo automaticamente la S-box inversa
PI_S_INV = [0] * 16
for indice, valore in enumerate(PI_S):
    PI_S_INV[valore] = indice

# P-box (Permutation-box): indica dove deve finire ciascun bit.
PI_P = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]


def get_round_keys(master_key_32bit):
    """
    Prende la chiave principale da 32 bit e ritaglia 5 sottochiavi da 16 bit.
    Ogni sottochiave si ottiene spostando una 'finestra' di 4 bit verso destra.
    """
    round_keys = []
    for r in range(1, 6): # r va da 1 a 5
        shift = 32 - (16 + 4 * (r - 1)) # calcola la finestra di lettura
        k_r = (master_key_32bit >> shift) & 0xFFFF # esegue shifting verso dx 
        round_keys.append(k_r)
    return round_keys


def apply_sbox_layer(state_16bit, sbox):
    """
    Prende i 16 bit di stato, li divide in 4 blocchetti da 4 bit ciascuno,
    e passa ciascun blocchetto dentro la S-box.
    """
    output = 0
    for i in range(4):
        shift = (3 - i) * 4 # shift per leggere il blocco giusto
        nibble = (state_16bit >> shift) & 0xF # isola i 4 bit
        output |= (sbox[nibble] << shift) # usa come indice nibble per cercare l'output giusto
    return output # restituisce tutti e 4 i blocchi dopo l'S-box


def apply_permutation(state_16bit, perm):
    """
    Legge i 16 bit uno ad uno e li sposta nella nuova posizione 
    indicata dalla lista 'perm'.
    """
    output = 0
    for i in range(16):
        bit = (state_16bit >> (15 - i)) & 1 # isola il bit in pos i 
        dest_pos = perm[i] # nuova pos dove mettere il bit i
        output |= (bit << (15 - dest_pos)) # bit i messo nella pos giusta
    return output # restituisce tutti e 4 i blocchi dopo la permutazione


def spn_encrypt(x, round_keys, N=4):
    """
    Cifratura: prende il testo in chiaro 'x' e lo trasforma in testo cifrato.
    """
    w = x  # Stato iniziale
    
    # Primi N-1 round (in questo caso i round 1, 2 e 3)
    for r in range(1, N):
        u = w ^ round_keys[r - 1]
        v = apply_sbox_layer(u, PI_S)
        w = apply_permutation(v, PI_P)
    
    # Ultimo round (round 4): identico ai precedenti ma SENZA la permutazione
    u_N = w ^ round_keys[N - 1]
    v_N = apply_sbox_layer(u_N, PI_S)
    
    # Whitening finale: un ultimo XOR con la chiave finale
    y = v_N ^ round_keys[N]
    
    return y


def spn_decrypt(y, round_keys, N=4):
    """
    Decifratura: fa esattamente i passi della cifratura ma al contrario,
    usando la S-box inversa.
    """
    # Rimuove l'ultimo step di Whitening
    v_N = y ^ round_keys[N]
    
    # Inverte la S-box dell'ultimo round
    u_N = apply_sbox_layer(v_N, PI_S_INV)
    
    # Rimuove la chiave del round 4
    w = u_N ^ round_keys[N - 1]
    
    # Esegue i round precedenti al contrario (dal 3 fino all'1)
    for r in range(N - 1, 0, -1):
        v = apply_permutation(w, PI_P)
        u = apply_sbox_layer(v, PI_S_INV)
        w = u ^ round_keys[r - 1]
    
    return w


# ==============================================================================
# TEST DEL CODICE CON VALORI CASUALI
# ==============================================================================
print("=== TEST SPN CON VALORI RANDOMICI ===")

# Genera una chiave maestra casuale da 32 bit 
K_master = random.randint(0, 0xFFFFFFFF)

# Genera un messaggio in chiaro casuale da 16 bit
x_plain = random.randint(0, 0xFFFF)

# Calcola le 5 sottochiavi
keys = get_round_keys(K_master)

# Cifra e poi decifra il messaggio
y_cipher = spn_encrypt(x_plain, keys)
x_dec    = spn_decrypt(y_cipher, keys)

# Prepara le stringhe in binario e in esadecimale
k_bin = format(K_master, '032b')
k_hex = format(K_master, '08X')

x_plain_bin = format(x_plain, '016b')
x_plain_hex = format(x_plain, '04X')

y_cipher_bin = format(y_cipher, '016b')
y_cipher_hex = format(y_cipher, '04X')

x_dec_bin = format(x_dec, '016b')
x_dec_hex = format(x_dec, '04X')

# Stampa i risultati unendo i pezzi
print("Chiave Master generata : " + k_bin + " (Hex: " + k_hex + ")")
print("Plaintext originale    : " + x_plain_bin + " (Hex: " + x_plain_hex + ")")
print("Ciphertext (cifrato)   : " + y_cipher_bin + " (Hex: " + y_cipher_hex + ")")
print("Plaintext decifrato    : " + x_dec_bin + " (Hex: " + x_dec_hex + ")")

# Controllo di sicurezza con un classico if
if x_plain == x_dec:
    print("\nVerifica superata: La decifratura ha ripristinato il messaggio originale senza errori!")
else:
    print("\nErrore: la decifratura non coincide!")