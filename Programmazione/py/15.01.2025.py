#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:16:28 2025

@author: valerio
"""

#il metodo split tiene conto degli spazi per carpire le parole all'interno di una stringa
#l differenza tra apice singolo e doppio: nell'ultimo caso tutti i caratteri che metto dentro la stringa sono da considerare normali
#(quindi anche se ci sono caratteri speciali vengono visti come normali)

a = "Questa, è la. striNga: più  noiosa dell'anno e questa no"
b=''

for x in a:
    if x.isalpha():
        b+=x.lower()
    else:
        b+=' '
print(b)




# In[]
a = "Questa, è la. striNga: più  noiosa dell'anno e questa no"

def lista_parole(a):
    
    b = []
    
    acc = { 'è': 'e', 'é':'e', 'ò':'o', 'ù':'u', 'à':'a', 'ì':'i'}
    
    for x in a:
        if x.isalpha(): #questa funzione controlla tutti i simboli dell'alafabeto
            x = x.lower()
            if x in acc:
                x = acc[x]
            elif  x < 'a' or x > 'z':
                continue    
            b.append(x.lower()) 
            # b += x.lower() # costo lineare nella dim di b
        else:
            #b += ' ' coto lineare
            b.append(' ')
            
    return ''.join(b).split()

# In[]

def firma(x):
    # ritorna la stringa delle lettere nella parola x ordinate in modo 
    # crescente
    return ''.join(sorted(x))

# In[]

nome_file = 'promessi_sposi.txt'

f = open(nome_file)


# costruire il dizionario delle firme
d ={} # d[k] = insime di parole con firma k

for line in f:
    # estrarre le parole da line
    for p in lista_parole(line):
        k = firma(p)
        if k in d:
            d[k].add(p)
        else:
            d[k] = set([p])
    

            
f.close()

# In[]


nome_file = 'promessi_sposi.txt'

f = open(nome_file)


# costruire il dizionario delle firme
d ={} # d[k] = insime di parole con firma k

for line in f:
    # estrarre le parole da line
    for p in lista_parole(line):
        k = firma(p)
        if k in d and p not in d[k]: #ci sono alternative a quest afunzione not in d[k] perchè se la lista è troppo grande andrà ad avere un costo lineare
        #a questo punto si usa il set come d[k] al posto di unsa lista. Il set è una struttura dati simile al dizionario perchè ha le chiavi ma non i valori.
        #posso eseguire delle operazioni insiemistiche: appartenenza, add, union
            d[k].append(p)
        else:
            d[k] = [p]
    

            
f.close()

# In[]

d_clean = {}

c = 0
for k in d:
    if len(d[k]) > 1:
        d_clean[k] = d[k]