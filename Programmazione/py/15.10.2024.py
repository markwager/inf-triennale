#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:25:16 2024

@author: valerio
"""


#da maiuscolo a minuscolo

c='C'

if (c>='A' and c<='Z'):
    delta=ord(c)-ord('A')
    cmin=chr(ord('a')+delta)
    print(cmin)
    
# In[funzioni]
#la funzione è uno strumento in grado di effettuare un riutilizzo di un programma invece di riprogrammarlo

def sqrt(x):#parametro formale
    g=x/2 #variabili locali
    c=0 #variabili locali
    eps, cmax= 0.0000000001, 1000
    while abs(g-x/g)>eps and c<cmax: 
        c=c+1
        g=(g+x/g)/2
    return g #manda all'esterno il valore g

ris=sqrt(20)#parametro attuale legato a quello formale con l'invocazione della funzione
print(ris)

# In[]

def sqrt(x, eps, c_max):#parametri
    g=x/2 #variabili locali
    c=0 #variabili locali
    while abs(g-x/g)>eps and c<c_max: 
        c=c+1
        g=(g+x/g)/2
    return g #manda all'esterno il valore g

ris=sqrt(20, 0.000000001, 1000)
#oppure
ris=sqrt(20, eps=0.000000001, c_max=1000)
print(ris)

# In[]

def sqrt(x, eps=0.001, c_max=100):#parametri con due valori di default
    g=x/2 #variabili locali
    c=0 #variabili locali
    while abs(g-x/g)>eps and c<c_max: 
        c=c+1
        g=(g+x/g)/2
    return g #manda all'esterno il valore g

ris=sqrt(20, 0.000000001, 1000)
print(ris)
#oppure
ris=sqrt(20) #l'utente inserisce solo il val
print(ris)
ris=sqrt(20, c_max=2)
print(ris)
ris=sqrt(c_max=2, x=20)
print(ris)

# In[ex]

def pal(x):
    i=0
    while i<(len(x)/2) and x[i]==x[len(x)-1-i]:
        i+=1
    
    if x[i]!=x[len(x)-1-i]:
        return False
    else:
        return True
            
print(pal('anna'))

# In[]

a='anna'
print(a[-2])
print(a[1:4]) #da 1 a 4-1
print(a[:4]) #da 0 a 4-1
print(a[1:3:2]) #da 1 a 3-1 a passo di 2 se lo step è negativo non vale nulla
print(a[::-1])
# In[]

def pal(x):
    return a==a[::-1]
            
print(pal('anna'))

#crea una nuova stringa nel caso in la parola è palindroma, nel caso non lo fosse ci sarbbe uno spreco di memoria e 





