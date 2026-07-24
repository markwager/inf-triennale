#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:09:40 2024

@author: valerio
"""

#ordinare date dalla più vecchia alla più recente

a=['09-12-2024', '10-12-2022', '18-10-2023']

def f(e): #si mette come funzione key per filtrare l'ordinamento
#si deve ritornare una tupla con la forma (anno-mese-giorno)

    return(e[6:], e[3:5], e[:2])

print(sorted(a, key=f))

# In[]

a=['09-12-2024', '10-12-2022', '18-10-2023']
b=[]

for e in a:
    b.append(e.split('-')[::-1])
b.sort()

print(b) 

for i in range(len(b)):
    b[i]='-'.join[i]

print(b)


# In[]


a=['09-12-2024', '10-12-2022', '18-10-2023']

b=[e.split('-')[::-1] for e in a] #comprensione di liste
b.sort() #ordina b in modo lessico grafico
#split è un metodo che consente di creare una lista contenente elementi splittati dalla lista originale secondo un separatore

print(b) 

for i in range(len(b)):
    b[i]='-'.join(b[i])

print(b)