#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:20:37 2025

@author: valerio
"""

"""
Scrivi una funzione che utilizzi sorted per ordinare una lista di numeri in ordine decrescente.
"""

def ordecr(L):
    lista=sorted(L, key= lambda x:-x)
    return lista

L=[1,2,3,4,5,6]
print(ordecr(L))

# In[]
def ordlen(L):
    lista1=sorted(L, key= lambda x: len(x)) 
    return lista1



L1=["addiokfdknf","baciami","cazzo","dario","elefaaaf","finocchio"]
print(ordecr(L1))

# In[]

"""
Usa sorted per ordinare una lista di tuple in base al secondo elemento di ciascuna tupla.
"""

def ordecr(L):
    lista=sorted(L, key= lambda x: x[1] )
    return lista



L=[(1, 5), (2, 1), (3, 7), (4, 2)]
print(ordecr(L))

# In[]

"""
Usa sorted per ordinare una lista di stringhe in ordine alfabetico, ignorando maiuscole e minuscole.
"""

def ordecr(L):
    lista=sorted(L, key= lambda x: x.lower() )
    return lista



L=["Banana", "mela", "Arancia", "ciliegia"]
print(ordecr(L))

# In[]

"""
Dato un dizionario, usa sorted per ottenere una lista delle chiavi ordinate in base ai valori.
"""

def ordecr(d):
    listasos=sorted(d, key= lambda x: d[x] )
    return listasos


d= {'a': 3, 'b': 1, 'c': 2}
print(ordecr(d))

# In[]

def ordecr(d):
    listasos=sorted(d, key= lambda x: d[x])
    listasos=[d[k] for k in listasos]
    return listasos


d= {'a': 3, 'b': 1, 'c': 2}
print(ordecr(d))

# In[]

"""
Ordinare numeri in una lista in ordine crescente
Usa il metodo .sort per ordinare una lista di numeri in ordine crescente.
"""

numeri = [8, 4, 6, 2, 9]
numeri.sort()
print(numeri)

# In[]

"""
Usa .sort per ordinare una lista di parole in ordine alfabetico inverso.
"""

parole = ["zebra", "mela", "banana", "ciliegia"]
parole.sort(reverse=True)
print(parole)

# In[]

"""
Usa .sort per ordinare una lista di tuple in base al primo elemento.
"""
coppie = [(4, 2), (1, 5), (3, 3), (2, 7)]
coppie.sort(key=lambda x: x[0])
print(coppie)

# In[]

"""
Usa .sort con un parametro lambda per ordinare una lista di parole in base alla loro lunghezza in ordine decrescente.
"""

parole = ["sole", "cielo", "mare", "montagna"]
parole.sort(key=lambda x: len(x), reverse=True)
print(parole)

# In[]

"""
Trasforma le chiavi di un dizionario in una lista e ordina la lista di chiavi in-place usando .sort basandoti sui valori del dizionario.
"""

diz = {'a': 3, 'b': 1, 'c': 2}
chiavi = list(diz.keys())
chiavi.sort(key= lambda x: diz[x])
print(chiavi)

# In[]

"""
Usa una lambda che contiene un ciclo for per calcolare il quadrato di ogni numero da 1 a 10.
"""

x=(lambda: [a**2 for a in range(1,11)])
print(x())

# In[]

"""
Usa una lambda con un ciclo for per concatenare la stringa "fruit_" a ciascuna parola in una lista di stringhe.
"""

words = ["apple", "banana", "cherry"]
stringa="fruits"
x=(lambda: [stringa+x for x in words])
print(x())

# In[]

"""
Usa una lambda con un ciclo for per creare una lista di tuple dove ciascuna contiene un numero e il suo quadrato.
"""

numbers = list(range(1, 6))
lista=[(x,x**2) for x in numbers]
print(lista)

#come si vede si può fare anche senza lambda

