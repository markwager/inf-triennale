#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:07:16 2024

@author: valerio
"""

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    n=len(a)
    #m=rx-lx è la dimensione dell'output
    b=sorted(a, key=t1) #tempo O(nlog(n)), spazio O(n)
    lx, rx=b[0][1], b[-1][1]
    i=0 #indice in b del prossimo punto da stampare
    for p in range(lx, rx+1):
        if i<n and p==b[i][1]:
            print([b[i][0]], end='')
            i+=1
        else:
            print('*', end='')

#complessità: O(nlog(n)+m) nel caso peggiore (m è per via del ciclo for)
#spazio O(n)

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
disegna_punti_su_retta(a)

# In[dizionario]

#il dizionario è una struttura dati che ci sonsente di fare ricerca in modo efficinete
#un dizionario è una struttura dati che consente di creare un mapping (associazione) tra due insiemi di dati
#chiave e valore sono gli insiemi per la ricerca
#ricerca di una chiave, aggiornamento chiave e cancellazione chiave
#queste operazioni sono efficienti (tempi medio costante)

a=[9, 2, 1, 8, 4] #insieme
b=[1, 7, 0, 8, 2] #insieme
#non ci sono ripetizioni

#voglio un algoritmo che calcoli a intersezione b
#c=[1,2,8]

#alg 1

c=[]

for e in a:
    if e in b:
        c.append(e)
        
print(c)

#complessità temporale O(n^2) nel caso peggiore e medio
#costo medio di ricerca nel caso medio
#
#e è b[0] 1 confronto
#e è b[1] 2 confronti
#e è b[2] 3 confronti
#...
#e è b[n-1] n confronti
#e non è in b n+1 confronti

#costo medio: somma di tutti i confronti (1+2+3+...+(n-1)+n+(n+1)))/(n+1)=((n+2)n/2(n+1))=O(n/2) circa


# In[]

#alg 2

a=[9, 2, 1, 8, 4] #insieme
b=[1, 7, 0, 8, 2] #insieme

#assumamiamo che len(a)==len(b)

a.sort()
b.sort()

i,j=0,0

c=[]

while i<len(a) and j<len(b):
    if a[i]==b[j]:
        c.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1
    else:
        j+=1

print(c)

#complessità temporale O(nlog(n)+m)
#complessità spaziale O(n) per via del metodo sort


# In[]

#ora si fa un algoritmo col mapping tra chiave e valori (k,v)

#d contiene (k0, v0), (k1, v1),
#proprietà: le chiavi sono univoche ki!=kj se i!=j
#le chiavi possono essere numeri, tuple o liste
#i valori everthing
#operazioni: dato un dizionario possiamo fare una:
#ricerca: k è una chiave del dizionario?
#
#lettura: data una chiave k voglio conoscere il valore associato a k
#
#aggiornamento: k,v se k è una chiave ne viene aggiornato il valore a v
#altrimenti (k,v) viene aggiunto al dizionario
#
#cancellazione: k, se k è una chiave elimina la coppia (k,v)
#eltrimenti errore


d={} #dizionario vuoto

d={5:'cinque', 'uno':1.0, 'due':(1,2)} #inizializzaione del dizionario
print(d, len(d)) #lunghezza è il numero di coppie

print(5 in d)#operazione di ricerca di chiave
print('5' in d)

print(d['uno'])#stampa il valore associato alla chiave 'uno'
#print(d[1]) da il keyerror perchè non c'è la chiave 1 nel dizionario

d['uno']='UNO' #aggiornato il valore associato a 'uno'
print(d)

d[10]='2x5' #nuova coppia chiave-valore
print(d)

del(d['uno'])
print(d)

#del(d['12']) key error

#queste op. in media hanno un costo costante:
#creazione del dizionario vuoto, ricerca, aggiornamento, lettura e cancellazione
#quindi quando si parlerà di costi di dizionari si parlerà sempre di costo medio (sia spaziale che temporale)

# In[risolviamo il problema dell'intersezione]

#alg 3

a=[9, 2, 1, 8, 4] #insieme
b=[1, 7, 0, 8, 2] #insieme

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
        
print(c)


#complessità:
#temporale: O(n) nel caso medio
#spaziale: O(n) sempre perchè crea srutture di appoggio

# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]

    lx=min(a, key=t1)[1]
    rx=max(a, key=t1)[1]
    
    d={}
    
    for nome, coordinata in a:
        d[coordinata]=nome
    
    for p in range(lx-1, rx+2): #tempo O(n)
        if p in d:
            print(d[p], end='')
        else:
            print('*', end='')
        print(c, end='') #tempo O(m)
    print('\nfine')
    
a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
print(disegna_punti_su_retta(a))









