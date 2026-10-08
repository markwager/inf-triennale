relazione={}
i=0
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for k in alfabeto:
    relazione[k]=i
    i+=1

print(relazione)

k=3
x="sonovalerio"

def encryption(x,k):
    y=""
    for i in range(len(x)):
        val_x=relazione[x[i]]
        val_y=(val_x+k)%26
        yi=alfabeto[val_y]
        y+=yi
    return y

y=encryption(x,k)
print("Testo cifrato:",y)

def decryption(y, k):
    x=""
    for i in range(len(y)):
        val_y=relazione[y[i]]
        val_x=(val_y-k)%26
        xi=alfabeto[val_x]
        x+=xi
    return x

ris=decryption(y,k)
print("Testo decifrato:",ris)
