#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:12:16 2024

@author: valerio
"""

#la soluzione + efficiente in termini di memoria(spazio) che di calcolo(tempo=numero di operazioni)
#si vogliono contare il numero di parole in una frase
a0='programmazione dei calcolatori con laboratorio'
a1='linguaggi di programmazione:c; python, java'


def lettera(i):
    return i >='a' and i<='z'

def conta_parole(a):
    '''
    Input: a una stringa (str di lungh 1)
    Return: num parole nella stringa
    
    Una parola è una sequenza massimale di caratteri alfabetici minuscoli
    '''
    #docstring
    #n=len(a)
    parole=0
    in_word=False
    for i in a:
        if lettera(i): #no 2 op, no 3, no 4 ma 5. Alcune volte sono 4. Queste sono costanti, cioè non dipendono da n. Quindi è una costante (non cambia il valore) c0
            if not in_word: #costante c1
                parole+=1 #3 operazioni, costante c2
                in_word=True #1 operazione`, costante c3
        else:
            if in_word==True: #costante c4
                in_word=False  #costante c3
        #la somma tra costanti è sempre una costante
        #il costo è quindi c*n+d=c*len(a)+d, dove d è il "contorno" del blocco, quindi il costo delle inizializzazioni dell'ultimo return
        #+ le inizializzazioni delle variabili. Tuttavia buttiamo i termini + piccoli perchè la funzione principale n*c cresce più velocemente
        #si possono buttare anche le costanti moltiplicative:c
        #quindi il costo della nostra funzione è O(n)
    return parole
        
print(conta_parole(a0))

# In[]




        
    
        
