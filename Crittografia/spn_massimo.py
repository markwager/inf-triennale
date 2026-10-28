import os, random
from collections import Counter

SBOX     = [0xE, 2, 1, 3, 0xD, 9, 0, 6, 0xF, 4, 5, 0xA, 8, 0xC, 7, 0xB]
SBOX_INV = [SBOX.index(i) for i in range(16)]
# permutazione dei bit (posizioni 1..16, bit 1 = MSB): il bit i va in posizione PERM[i]
PERM = [None, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
PERM_INV = [0] * 17 
for i in range(1, 17):
    PERM_INV[PERM[i]] = i
# permutazione inversa

NR = 4  # numero di round

def sub(x, box):
    return sum(box[(x >> (4 * i)) & 0xF] << (4 * i) for i in range(4))
'''applica le S-box a tutto il blocco (4 nibble da 4 bit) 
    per ogni i da 0 a 3, prende il nibble i-esimo di x,sposta a destra i bit per portare 
    il nibble corrente in fondo, applica una maschera (0xF) (1111 in binario) per isolare solo 
    quei 4 bit, passa il valore alla s-box e lo rimette nella posizione originale. 
    sum ricompone la lista dinibble in un intero a 16 bit.'''

def permute(x, table):
    y = 0
    for i in range(1, 17):
        if (x >> (16 - i)) & 1:
            y |= 1 << (16 - table[i])
    return y
'''per ogni posizione i da 1 a 16, legge il bit i-esimo di x contando da sinistra
    se vale 1 accende nel risultato il bit nella nuova poszione table[i] 
    con 1 << (16- table[i])
    gli zeri non serve spostarli perché y è inizializzato a 0.'''

def encrypt(p, keys):
    """keys = 5 sottochiavi da 16 bit (chiave totale 80 bit)."""
    x = p
    for r in range(NR - 1):
        x = permute(sub(x ^ keys[r], SBOX), PERM)
    x = sub(x ^ keys[NR - 1], SBOX) ^ keys[NR]   # ultimo round: niente permutazione
    return x
'''applica NR-1 round di SPN: 
    1) XOR con la sottochiave (x ^ keys[r])
    2) applica le S-box (sub(..., SBOX))
    3) applica la permutazione (permute(..., PERM))

    l'ultimo round non ha la permutazione, bensì un altro XOR con la sottochiave finale.'''

def decrypt(c, keys):
    x = sub(c ^ keys[NR], SBOX_INV) ^ keys[NR - 1]
    for r in range(NR - 2, -1, -1):
        x = sub(permute(x, PERM_INV), SBOX_INV) ^ keys[r]
    return x
''' fa letteralmente l'inverso di encrypt, partendo dall'ultimo round e andando a ritroso:'''

def key_from_hex(text):
    """Chiave da 80 bit scritta come 20 cifre esadecimali -> [K1..K5] da 16 bit.
    Accetta prefisso 0x e separatori (spazi, '-', '_')."""
    t = text.strip().lower().removeprefix("0x")
    t = t.replace(" ", "").replace("-", "").replace("_", "")
    if len(t) != 20:
        raise ValueError(f"servono 20 cifre esadecimali (80 bit), ne hai date {len(t)}")
    try:
        k = int(t, 16) ## converte la stringa in un intero base 16
    except ValueError:
        raise ValueError("la chiave puo' contenere solo cifre 0-9 e lettere a-f")
    return [(k >> (16 * (4 - i))) & 0xFFFF for i in range(5)]
    '''estrae le 5 sottochiavi da 16 bit ciascuna, partendo dai bit più significativi.
    e le maschera con =xFFFF per tagliare i bit che non sono significativi.'''

def encrypt_message(msg: str, keys):
    """ECB su blocchi da 2 byte."""
    b = msg.encode() #il messaggio viene codificato in bytes
    if len(b) % 2: b += b"\x00" #aggiunge un byte nullo di padding se il numero di bytes è dispari
    return [encrypt((b[i] << 8) | b[i + 1], keys) for i in range(0, len(b), 2)]
    '''for i in range(0, len(b), 2) genera gli indici con passo 2, quindi prende i byte a coppie
        (b[i] << 8) | b[i + 1] unisce i due byte: b[i] << 8) sposta il primo byte di 8 bit a sinistra, 
        e | b[i + 1] fa l'OR con il secondo byte mettendolo nella metà bassa del risultato.'''

def decrypt_message(blocks, keys):
    out = bytearray()
    for c in blocks:
        p = decrypt(c, keys); out += bytes([p >> 8, p & 0xFF])
    return out.rstrip(b"\x00").decode(errors="replace")
'''fa il percorso inverso di encrypt.'''