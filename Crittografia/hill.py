alfabeto = "abcdefghijklmnopqrstuvwxyz"
relazione = {}
for i in range(26):
    relazione[alfabeto[i]] = i

# Matrice chiave K (2x2) usata nell'esempio del libro
K = [
    [11, 8],
    [3,  7]
]

# Matrice inversa K^-1 (2x2) usata per decifrare
K_inv = [
    [7,  18],
    [23, 11]
]

m = 2

# Funzione per moltiplicare un vettore 1xm per una matrice mxm (modulo 26)
def moltiplica_vettore_matrice(vettore, matrice):
    risultato = []
    for colonna in range(m):
        somma = 0
        for riga in range(m):
            somma += vettore[riga] * matrice[riga][colonna]
        risultato.append(somma % 26)
    return risultato

def encryption(testo, matrice):
    y = ""
    # Aggiungiamo un padding se la lunghezza del testo non è multipla di m
    resto = len(testo) % m
    if resto != 0:
        testo += "x" * (m - resto)
        
    for i in range(0, len(testo), m):
        blocco = testo[i:i+m]
        vettore_x = []
        for carattere in blocco:
            vettore_x.append(relazione[carattere])
            
        # y = xK mod 26
        vettore_y = moltiplica_vettore_matrice(vettore_x, matrice)
        
        for numero in vettore_y:
            y += alfabeto[numero]
    return y

def decryption(testo_cifrato, matrice_inversa):
    x = ""
    for i in range(0, len(testo_cifrato), m):
        blocco = testo_cifrato[i:i+m]
        vettore_y = []
        for carattere in blocco:
            vettore_y.append(relazione[carattere])
            
        # x = yK^-1 mod 26
        vettore_x = moltiplica_vettore_matrice(vettore_y, matrice_inversa)
        
        for numero in vettore_x:
            x += alfabeto[numero]
    return x

# Esecuzione del test (senza f-string)
testo_originale = "july"

testo_cifrato = encryption(testo_originale, K)
print("Testo cifrato:", testo_cifrato.upper())

testo_decifrato = decryption(testo_cifrato, K_inv)
print("Testo decifrato:", testo_decifrato)