#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:20:02 2025

@author: valerio
"""

"""
Scrivere una funzione, denominata is_symmetric, che riceva in input una lista di liste di numeri e restituisca True se e solo se la lista può
rappresentare una matrice simmetrica (ovvero una matrice quadrata dove ogni elemento M[i][j] è uguale a M[j][i]).
"""

def is_symmetric(L):
    
    for row in L:
        if len(row) != len(L):
            return False

    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j]!=L[j][i]:
                return False
    return True  


L=[[1, 2, 3], [2, 4, 5], [3, 5, 6]] #con la prima diventa True
L=[[1, 0], [2, 1]] #con la seconda ritorna False
print((is_symmetric(L)))

# In[]

"""
Esercizio: Scrivere una funzione, denominata is_diagonal_matrix, che riceva in input una lista di liste di numeri e restituisca True se e solo
se la lista può rappresentare una matrice diagonale (ovvero una matrice quadrata dove tutti gli elementi al di fuori della diagonale principale
sono zero).
"""

def is_diagonal_matrix(L):
    for row in L:
        if len(row) != len(L):
            return False

        for i in range(len(L)):
            for j in range(len(L)):
                if L[i][j]!=0 and (i!=j):
                    return False
        return True  

    

L=[[1, 0, 0], [0, 5, 0], [0, 0, 9]]
print(is_diagonal_matrix(L))

# In[]

"""
Esercizio: Scrivere una funzione, denominata count_words, che riceva una stringa e restituisca un dizionario in cui le chiavi sono le parole
presenti nella stringa e i valori rappresentano il numero di volte che ogni parola compare.
"""

def count_words(stringa):
    
    d = {}
    
    parole = stringa.split()
    
    for parola in parole:
        if parola in d:
            d[parola] += 1  
        else:
            d[parola] = 1
    
    return d


stringa="ciao mondo ciao"
print(count_words(stringa))


# In[]

"""
Esercizio: Scrivere una funzione, denominata reverse_string, che riceva in input una stringa e restituisca la stessa stringa invertita.
"""

def reverse_string(stringa):
    stringa=stringa[::-1]
    
    return stringa
    
    
stringa="ciao"
print(reverse_string(stringa))





