#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:08:27 2025

@author: valerio
"""

"""
la funzione print stampa tutti i primi argomenti fino al primo argomento dichiarato per nome
ci sono:
    *values(////)
    sep (argomento def per nome) è lo spazio
    end carattere che sta alla fine della stringa
    ecc....
    
    Lo star (*) ha il significato in questo caso che gli argomenti sono in numero variabile
    Anche le funzioni min max hanno questa cosa dello star
"""

def concatena(*args):
    a=''
    for x in args:
        a+=x
    return(a)
        
    
print(concatena('uno','sas'))

#non è un metodo efficinete perchè la concatenazione crea sempre una nuova stringa
#si avrebbe un costo di n*n poichè se l'ultima stringa è lunga n, ed è dentro un for, allora si ha un costo quadratico-->O(n**2)

# In[]

#il metodo più efficiente è usare il metodo join perchè ha costo lineare

def concatena(*args):
    return ''.join(args)
print(concatena('sas',"sus"))

# In[]

b=["uno", "due", "tre"]
print(b)

#voglio stampare il contenuto dells lista senza virgola

print(' '.join(b))
#ecco il metodo

for x in b:
    print(x, end=" ")
print()

print(*b) #star b spacchetta l'iterabile b

# In[]

import matplotlib.pyplot as plt#il nome per utilizzare le funioni non è più "math.", "ma m."
#si può anche importare solo una funzione della libreria usando "from math import tan"
#un modulo si può dividere in più sottomoduli

p=[(3,1), (10,-3), (2,6), (8,-6)]

#voglio rappreentare questi punti nel piano
#in py si utilizza la libreria (in realtà moduli si chiamano)
#si devono importare 

x=[x0 for x0, _ in p] #mettiamo "_" nel momento in cui non ci serve una variabile aggiuntiva per l'unpacking
y=[x1 for _,x1 in p]
plt.plot(x,y)

# In[]
#star p spacchetta la tupla e crea tanti oggetti quanti sono gli elementi della tupla
#zip star p spacchetta gli elementi della tupla e zippa gli elementi interni
#zip(*p) è zip((3,1), (10,-3), (2,6), (8,-6))

for x in zip(*p): #zip ritorna un'iterabile
    print(x)

# In[]

#a questo punto posso usare ciò per fare unoi spacchettamento

x,y=list(zip(*p))
plt.plot(x,y)

# In[]

#come leggere i file su py

f=open(....)#si mette dentro il file ma deve essere nella directory giusta
#questo file è aperto in modalità lettura
for line in f:
    print(line, end='') #se stampa degli spazi in pià è colpa della funzione print
f.close()
#con questo leggo riga per riga il file
#con il close posso modificare il file a parte perchp altrimenti non me lo farebbe modificare se non ci fosse close
#il close è praticolarmente importante per l'operazione di scrittura, altrimenti non modifica

# In[]

f=open(...,"w") #in modalità scrittura, crea un nuovo file

f.write(...)
f.close()
