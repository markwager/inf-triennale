#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:12:51 2024

@author: valerio
"""

#ho due liste
nomi=['A','B','A','C','B','D','A','C'] #i punti ripetuti vuol dire che si sono spostati
pos=[3, 1, 9, 0, 10, 2, 4, 2]

#al tempo i pos[i] è la nuova posizione di nomi[i]

#qual è l'ultima configurazione dei punti? Ovvero voglio sapere la posizione dei punti
#alla fine della serie temporale

#d[k]=p se il punto k si trova in posizione p
n=len(nomi)

d={}

for i in range(n):
    d[nomi[i]]=pos[i] #O(1) in media

print(d)

#complessità temporale: O(n) medio

# In[]

#la funzione zip ritorna ad ogni iterazione la prima volta il primo elemento di nomi e pos, il secondo, il terzo... fino ad esaurimento

d={}

for nome, p in zip(nomi, pos):
    print(nome,p)

# In[]

d={}

for nome, p in zip(nomi, pos):
    d[nome]=p
    print(d)

# In[]

#i metodi dei dizionari

print(d.keys()) #restituisce le chiavi
print(d.values()) #restituisce i valori
print(d.items()) #restituisce le coppie

# In[]

#per ogni posizione voglio sapere i punti che sono passati in quelle posizioni

nomi=['A','B','A','C','B','D','A','C'] #i punti ripetuti vuol dire che si sono spostati
pos=[3, 1, 9, 0, 10, 2, 4, 2]

d={}

#d[nome]=lista delle posizioni occupate da nome

for nome, p in zip(nomi, pos):
    if nome in d:
        d[nome].append(p)
    else:
        d[nome]=[p]
print(d)
        
#questo test lo possiamo evitare usando il merodo get
# In[]

d={'a':2, 'b':1}

print(d.get('a'))
print(d.get('c')) #ritorna None perchè non c'è la chiave. Si può modificare il valore None (che è di default)
print(d.get('c',0))

# In[]

nomi=['A','B','A','C','B','D','A','C'] #i punti ripetuti vuol dire che si sono spostati
pos=[3, 1, 9, 0, 10, 2, 4, 2]

d={}

#d[k]=somma delle posiioni in cui compare k

for nome, p in zip(nomi, pos):
    if nome in d:
        d[nome]+=p
    else:
        d[nome]=p

print(d)

# In[]

#si usa il metodo get per evitare le condizioni

d={}

for nome, p in zip(nomi,pos):
    d[nome]=d.get(nome,0)+p
print(d)


# In[]
'''
nomi=['A','B','A','C','B','D','A','C'] #i punti ripetuti vuol dire che si sono spostati
pos=[3, 1, 9, 0, 10, 2, 4, 2]

d={}

for nome, p in zip(nomi, pos):
    d[nome]=d.get(nome,[]).append(p)
print(d)
        
#questo test lo possiamo evitare usando il merodo get
'''

# In[]

d={'A':9, 'B':3, 'C':3, 'D':2, 'E':9}
#d_inv[v]: [lista di chiavi di d che hanno per valore v]

d_inv={}

for k in d:
    v=d[k]
    if v in d_inv:
        d_inv[v].append(k)
    else:
        d_inv[v]=[k]
print(d_inv)


# In[]

d={'A':9, 'B':3, 'C':3, 'D':2, 'E':9}
#d_inv[v]: [lista di chiavi di d che hanno per valore v]

d_inv={}

for k, v in zip(d.keys(), d.values()):
    if v in d_inv:
        d_inv[v].append(k)
    else:
        d_inv[v]=[k]

print(d_inv)
    
# In[]

def intersec(a,b):
    #assumamiamo che len(a)==len(b)

    da, db={}, {}

    c=[]

    for e in a: #tempo e spazio O(n)
        da[e]=None #non mi interessa il valore
        
    for e in b:#same
        db[e]=None #O(1) tempo nel costo medio

    for e in da: #itera sulle chiavi del dizionario
        if e in db: #O(1) nel caso medio
            c.append(e)
            
    return c

a=[9, 2, 1, 8, 4] #insieme
b=[1, 7, 0, 8, 2, 76, 90] #insieme

c=intersec(a, b)
print(c)

# In[]

#voglio restituire un dizionario d in cui si hanno le chiavi in comune
def intersezione(d0, d1):
    '''
    Input: d0 d1 dizionari
    Output: d dizionario le cui chiavi sono quelle sia in d0
        che in d1
    '''
    d = {}
    
    # n, m = len(d0), len(d1)
    
    if len(d0) < len(d1):
        d0, d1 = d0, d1
    else:
        d0, d1 = d1, d0
        
    
    for e in d0:  # per min(n,m) volte
        if e in d1:  # O(1) tempo nel caso medio
            d[e] = d0[e]
    
    # complessità temporale O(min(len(d0), len(d1))) perchè così è più efficiente iterare su un dizionario più piccolo
    
    return d

d0 = {'a': None, 'b': None, 'c':None, 'd':None}
d1 = {'a': None, 'b': None}

print(intersezione(d0,d1))
    