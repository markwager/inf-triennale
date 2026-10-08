alfabeto = "abcdefghijklmnopqrstuvwxyz"
chiave   = "XNYAHPOGZQWBTSFLRCVMUEKJDI"

relazione_cifratura = {}
relazione_decifratura = {}

for i in range(26):
    lettera_chiara = alfabeto[i]
    lettera_cifrata = chiave[i]
    
    relazione_cifratura[lettera_chiara] = lettera_cifrata
    relazione_decifratura[lettera_cifrata] = lettera_chiara

def encryption(testo):
    y = ""
    for carattere in testo:
        if carattere in relazione_cifratura:
            y += relazione_cifratura[carattere]
        else:
            y += carattere
    return y

def decryption(testo_cifrato):
    x = ""
    for carattere in testo_cifrato:
        if carattere in relazione_decifratura:
            x += relazione_decifratura[carattere]
        else:
            x += carattere
    return x

# Esecuzione del test senza f-string
x = "cryptography"
y = encryption(x)

print("Testo cifrato:", y)

x_recuperato = decryption(y)
print("Testo decifrato:", x_recuperato)