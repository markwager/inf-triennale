#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:14:18 2024

@author: valerio
"""

def find_root(x, power, epsilon):#la funzione è un oggetto di prima classe:può essere trattata come un oggetto di qualsiasi tipo
# Trova l'intervallo contenente la risposta
    if x < 0 and power%2 == 0:
        return None #I numeri negativi non hanno radici pari
    low = min(-1, x)
    high = max(1, x)
    # Usa la ricerca per bisezione
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

print(find_root(25, 2, 0.001))

# In[]

#Usate la funzione find_root della Figura 4.3 per stampare la somma delle approssimazioni alla radice quadrata di 25,
#alla radice cubica di -8 e alla radice quarta di 16. Usate 0.001 come epsilon.

def find_root(x, power, epsilon):
# Trova l'intervallo contenente la risposta
    if x < 0 and power%2 == 0:
        return None #I numeri negativi non hanno radici pari
    low = min(-1, x)
    high = max(1, x)
    # Usa la ricerca per bisezione
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
    

print((find_root(-8, 3, 0.001)+(find_root(25, 2, 0.001))+(find_root(16, 4, 0.001))))

# In[]

#Scrivete una funzione is_in che accetti come argomenti due stringhe e restituisca True se una delle due stringhe compare all’interno dell’altra, False altrimenti.
#Suggerimento: potete usare l’operatore in per le str.

def is_in(str1,str2):
    if(str1 in str2):
        return True
    else:
        return False

print(is_in('iao', 'ciao'))

# In[]

#Scrivete una funzione mult che accetti come argomenti uno o due int. Se chiamata con due argomenti,
#la funzione stampa il loro prodotto. Se è chiamata con un solo argomento, stampa quello.

def mult(intero):
    return intero

print(mult('ciao'))

# In[]

def mean(*args):
    # Assume che ci sia almeno un argomento
    # e che tutti gli argomenti siano numeri
    # Restituisce la media degli argomenti
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1,2,3))

# In[]

#Scrivete un’espressione lambda che abbia due parametri numerici. Se il secondo argomento è uguale a zero,
#deve restituire None; altrimenti deve restituire il valore della divisione del primo argomento per il secondo.
#Suggerimento: usate un’espressione condizionale.

print((lambda num1, num2: None if num2 == num1 else num1/num2)(10, 5))#lambda è una funzione anonima (cioè una funzione slegata da un nome)
