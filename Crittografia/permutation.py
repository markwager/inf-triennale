# La chiave è una lista di indici che indica come mescolare le posizioni
# Equivalente a pi = [3, 5, 1, 6, 4, 2] del libro (con base 0 anziché base 1)
pi = [2, 4, 0, 5, 3, 1]
m = len(pi)

# Calcoliamo la permutazione inversa dinamicamente
# Inizializziamo una lista di zeri grande quanto m
pi_inversa = [0, 0, 0, 0, 0, 0]

for i in range(m):
    posizione_destinazione = pi[i]
    pi_inversa[posizione_destinazione] = i

def encryption(testo):
    y = ""
    # Il testo deve essere divisibile per m. 
    # Aggiungiamo un "padding" (carattere 'x') se necessario.
    resto = len(testo) % m
    if resto != 0:
        testo += "x" * (m - resto)
        
    # Scorriamo il testo saltando di m in m
    for i in range(0, len(testo), m):
        blocco = testo[i:i+m]
        # Mescoliamo i caratteri del singolo blocco usando pi
        for j in range(m):
            y += blocco[pi[j]]
            
    return y

def decryption(testo_cifrato):
    x = ""
    # Scorriamo il testo cifrato saltando di m in m
    for i in range(0, len(testo_cifrato), m):
        blocco = testo_cifrato[i:i+m]
        # Riordiniamo i caratteri usando pi_inversa
        for j in range(m):
            x += blocco[pi_inversa[j]]
            
    return x

# Esecuzione del test (senza f-string)
testo_originale = "shesellsseashellsbytheseashore"

testo_cifrato = encryption(testo_originale)
print("Testo cifrato:", testo_cifrato.upper())

testo_decifrato = decryption(testo_cifrato)
print("Testo decifrato:", testo_decifrato)