#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:27:16 2024

@author: valerio
"""

def g(L, e):
    """L è una lista di int, e è un int"""
    for i in range(100):
        for e1 in L: 
            if e1 == e:
                return True
    return False
#complessità temporale è: O(n), dove n=len(L)


# In[]

def h(L, e):
    """L è una lista di int, e è un int"""
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False

#la complessità temporale è: O(n*e), dove n=len(L) e e sarebbe e-1 (ma si toglie l'1 perchè non serve)

# In[]

#O(1) tempo di esecuzione costante.
#O(log n) tempo di esecuzione logaritmico.
#O(n) tempo di esecuzione lineare.
#O(n log n) tempo di esecuzione log-lineare.
#O(n^k) tempo di esecuzione polinomiale. Notate che k è una costante.
#O(c^n) tempo di esecuzione esponenziale. Qui una costante è elevata a un esponente dipendente dalle dimensioni dell’input.

def int_to_str(i):
    """Assume che i sia un int non negativo
       Restituisce una rappresentazione a stringa
           decimale di i"""
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result
print(int_to_str(3))
#complessità temporale è Theta(log(i)) perchè c'è i//10

def add_digits(n):
    """Assume che n sia un int non negativo
       Restituisce la somma delle cifre in n"""
    string_rep = int_to_str(n)
    val = 0
    for c in string_rep:
        val += int(c)
    return val

#la complessità temporale è Theta(log(n))+Theta(log(n)) (la prima provenienete da dalla funzione di prima e la seconda dal ciclo)

# In[]

#Molti algoritmi che hanno a che fare con liste o altri tipi di sequenze sono lineari, perché toccano ciascun elemento
#della sequenza un numero di volte costante (maggiore di 0).

def add_digitss(s):
    """Assume che s sia una stringa di cifre
       Restituisce la somma delle cifre in s"""
    val = 0
    for c in s:
        val += int(c)
    return val
#complessità temporale: O(n), dove n=len(s)

def factorial(x):
    """Assume che x sia un int positivo
       Restituisce x!"""
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
#complessità temporale: O(x) perchè è una funzione ricorsiva (notare che non ci sono loop evidenti)

# In[]

#Gli algoritmi polinomiali di uso più comune sono quelli quadratici, la cui complessità, cioè, cresce come il quadrato delle
#dimensioni dei loro input.

def is_subset(L1, L2):
    """Assume che L1 e L2 siano liste.
       Restituisce True se ogni elemento di L1
           è anche elemento di L2, False altrimenti."""
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
#complessità temporale: Theta(n)*Theta(l), dove n=len(L1) e l=len(L2)

# In[]

#Molti problemi importanti sono intrinsecamente esponenziali, cioè risolverli completamente può richiedere un tempo
#che cresce esponenzialmente al crescere delle dimensioni dell’input.

def get_binary_rep(n, num_digits):
    """Assume che n e numDigits siano int non negativi
       Restituisce una str di lunghezza numDigits che
           è una rappresentazione binaria di n"""
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > num_digits:
        raise ValueError('cifre insufficienti')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result
def gen_powerset(L):
    """Assume che L sia una lista
       Restituisce una list ache contiene tutte le
           possibili combinazioni degli elementi di L.
           Per esempio, se L è [1, 2] restituirà una lista
           con gli elementi [], [1], [2] e [1,2]."""
    powerset = []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_rep(i, len(L))
        subset = []
        for j in range(len(L)):
            if bin_str[j]== '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

#complessità temporale: O(2^n), dove n=len(L). Questo perchè perchè c'è un for che va da 0 fino a (2^n)-1



