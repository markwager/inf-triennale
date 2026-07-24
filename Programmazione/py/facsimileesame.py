#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:33:11 2025

@author: valerio
"""

L=[1, 2, 3, 3.14, 2.21, 9.1, "ciao", "sono", "valerio"]
interi=[]
stringhe=[]
virgvar=[]
k=3


for a in range(len(L)):
    if type(L[a])==int:
        interi.append(L[a])
    elif type(L[a])==str:
        stringhe.append(L[a])
    else:
        virgvar.append(L[a])
    if len(interi) == k and len(virgvar) == k and len(stringhe) == k:
        break
        
print(interi)
print(stringhe)
print(virgvar)

for interi, stringhe, virgvar in zip(interi, stringhe, virgvar):
    print(interi, stringhe, virgvar)

# In[]

def ltype(a):
    
    interi=[n for n in a if type(n)==int]
    virgmob=[v for v in a if type(v)==float]
    stringhe=[s for s in a if type(s)==str]
    
    for numeri, parole, nvirg in zip(interi, stringhe, virgmob):
        print(numeri, parole, nvirg)

a=["cacca", 23, 2.71, "pipì", 444, 3.14]
ltype(a)

#costo spaziale: O(n)
#costo temporale: O(n)
