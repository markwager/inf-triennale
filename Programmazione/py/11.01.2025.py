#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:14:42 2025

@author: valerio
"""

import matplotlib.pyplot as plt


nome_file = 'promessi_sposi.txt'

f = open(nome_file)

occ = {} # occ[c] = numero di volte in cui compare c in f
        # c deve essere un carattere alfabetico minuscolo
        # è, é -> e
        # ù -> u
        # ...
#usiamo il dizionario semplicemente cosè aumentiamo il valore associato alla chiave (occorrenze) 

for line in f:
    for x in line:
        # x è la potenziale chiave di occ (potrebbe essere un char non alfabetico o non minuscolo)
        if not x.isalpha() or x in ('ã','ˆ', 'â'):
            continue #si usa dentro i cicli e si passa all'iterazione successiva
        # x è alfabetico, può essere accentato
        if x.isupper(): # verifica se x è maiuscolo (considera le accentate) o lo facciamo con un intervallo
            x = x.lower()
        # x è una lettera minuscola non accentata
        if x in occ:
            occ[x] += 1
        else:
            occ[x] = 1
            
f.close()

#plt.bar(occ.keys(), occ.values())

X, Y = list(zip(*sorted(occ.items(), key=lambda e: e[1], reverse=True)))

# da valore assoluto a percentuale
tot_lettere = sum(Y)
Y = [ 100*y/tot_lettere for y in Y ]

plt.bar(X, Y)

# In[]

# Scrivere un programma che prenda in input una stringa k e ritorni
# tutti gli anagrammi di questa lista.
#
# Si utilizzi il file promessi_sposi.txt come fonte delle parole della
# lingua italiana
#
# La firma di una parola è la stringa ottenuta ordinando i caratteri della
# stringa
#
# Due stringhe sono una anagramma dell'altro se hanno la stessa firma
#
# afasd -> aadfs  (firma della stringa)
# faads -> aadfs
#
# Sia:
#   d[f] = lista di tutte le parole nel dataset che hanno per firma f
#
# Quindi d[firma(k)] è quanto richiesto dal problema 