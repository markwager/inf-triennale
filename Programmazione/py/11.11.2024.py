#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:00:40 2024

@author: valerio
"""


#ordinamneto per fusione fa sì che possa ordinare due sequenze ordinate tra loro
#confrontiamo gli elementi della prima sequenza con la seconda, eliminando poi dalla sequenza l'elemento minimo inserito nella
#nuova lista. Si incrementa la successione della lista 1 o 2 in base agli elementi inseriti nella nuova lista

#[algoritmo di fusione]
a=[0, 5, 8, 10, 11, 11, 14]
b=[1, 2, 6, 6, 6, 9 ,10]
c=[]

i, j=0, 0

while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

while i<len(a):
    c.append(a[i])
    i+=1

while j<len(b):
    c.append(b[j])
    j+=1
    
print(c)
#complessità spaziale: O(1) (c non si calcola perchè è output)
#complessità temporale: O(n)=len(a)+len(b)

# In[]

def merge(a, lx, cx, rx):
    '''
    lx, cx e rx sono parametri in a tale che
    lx<=cx<=rx con la proprietà che a[lx:cx] e a[cx:rx] sono ordinati
    
    output: None
    '''

    c=[]

    i, j=lx, cx

    while i<cx and j<rx:
        if a[i]<a[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(a[j])
            j+=1

    while i<cx:
        c.append(a[i])
        i+=1
        
    while j<rx:
        c.append(a[j])
        j+=1
        
    i=lx
    for e in c:
        a[i]=e
        i+=1
        
a=[10, 21, 0, 30 ,34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge(a, 3, 7, 12)
print(c)

#complessità temporale: O(n) per via della lunghezza della sottosequenza da ordinare

#complessità spaziale: O(n) per via della lista a

# In[]
#utilità algoritmo: data una sequenza di numeri, si divide (così avendo n/2 successioni), si ordinanano e poi si fondono.
#Per ordinare una delle due parti si divide a metà, si ordinano e si mettono insieme. Arrivo a una sequnza composta da una coppia
#di elementi e poi fino ad un elemento. Si hanno una sequenza di ordine 1 che sono quindi già ordinate.
#Dopodichè si usa l'algoritmo di prima (algoritmo di fusione) per ordinare

#[merge_sort]

def merge_sort(a, lx=0, rx=None): #non posso assegnare a un prametro il valore di un altro parametro
     
    if rx==None:
        rx=len(a)
    
    '''
    si può inserie una lista
    o una successione
    lx e rx (indice sx e dx)
    output: None
    effetto collaterale: ordinare in loco gli elementi di a[lx:rx] (cioè modificare la lista a)
    '''
    
    if lx+1 >= rx: #caso base
        return None
    
    cx=(lx+rx)//2
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    
    merge(a, lx, cx, rx)
    
#ordinare a[:n/2] e poi a[n/2:]
#fondere tra sottolistre consecutive
#ricorsione della funzione
#ci saranno due indici che descrivono gli intervalli da fondere

a=[10, 21, 0, 30 ,34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge_sort(a)
print(a)

#complessità temporale: O(log(n)*n)
#complessità spaziale: funzioni ricorsive chiamate (log(n)) per via delle sottosuccessioni ordinate) + lista di appoggio c (O(n))
#ma effettivamente è O(log(n)+n)=O(n)