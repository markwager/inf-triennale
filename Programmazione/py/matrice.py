#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:02:36 2025

@author: valerio
"""

i=int(input("Inserisci numero di righe: "))
j=int(input("Inserisci numero di colonne: "))

for x in range(i):
    for y in range(j):
        print("x", end=" ")
    print("\n")
    
#matrix con 10 nrighe e 4 colonne

# In[creazione statica di matrice]

matrix=[
        
    [0,0,0]
    [0,0,0]
    [0,0,0]        
    
]

# In[creazione dinamica di matrice]

i=int(input("Inserisci numero di righe: "))
j=int(input("Inserisci numero di colonne: "))

matrix=[["x" for x in range(i)] for y in range(j)]
print(matrix)

print(matrix[0][1]) #riga 0 colonna 1

for riga0 in matrix:
    print(riga0)

for riga1 in matrix:
    for e in riga1:
        print(e, end=" ")
    print("\n")
    
# In[quella di prima senza list comprehension]

i=int(input("Inserisci numero di righe: "))
j=int(input("Inserisci numero di colonne: "))

matrix=[]

for riga in range(i):
    riga=[]
    for colonna in range(j):
        riga.append(0)
    matrix.append(riga)
        








