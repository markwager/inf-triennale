#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:55:17 2024

@author: valerio
"""

def deep_copy(a):
    
    b = []
    for e in a:
        if type(e) != list:
            b.append(e)
        else:
            b.append(deep_copy(e))
    return b

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]
b = deep_copy(a)
print(b)
print(id(b)==id(a))
#questo programma ritorna un alias ma di un nuovo oggetto

#complessità temporale: T(n)=sommatoria di T(ne) dove ne è il num di elementi in e ed in tutte le sue liste annidate oppure
#è 1 se e non è lista. La sommatoria è uguale a n, dove n è il numero di elementi complessivi (perchè si esplodono tutte le liste per ottenere tutti valori scalari)
#La funzione è quindi lineare
#comlessità spaziale: O(n) perchè dipende dal numero di frame chiamati nella pila

#la dimensione dell'input è data dal numero degli elementi scalari in a ed in tutte le sottoliste annidate 

# In[]

#conviene ordinare e poi ricercare perchè si ha un costo logaritmico
#ma quanto costa l'ordinamento?
#algortimo di ordinamento per fusione fa si che il costo sia O(nlogn + mlogn)
