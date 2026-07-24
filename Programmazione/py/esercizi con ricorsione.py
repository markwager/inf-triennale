#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:51:50 2025

@author: valerio
"""


def somma_lista(L):
    
    count = 0  # Inizializza il contatore una sola volta
    for i in L:
        if type(i) == int:
            count += i  # Aggiungi direttamente il valore intero
        else:
            count += somma_lista(i)  # Ricorsione sulla sottolista
    return count


L = [1, [2, 3], 4, [5, [6, 7]]]
print(somma_lista(L))  # Deve restituire 28

# In[]

def conta_occurrences(L,n):
    
    count=0

    for i in L:
        if type(i)!=list:
            if i==n:
                count+=1
        else:
            count+=conta_occurrences(i,n)
    
    return count

n=2
L = [1, 2, [3, 4, [5, 2]], 2]
print(conta_occurrences(L, n))  # Deve restituire 3

# In[]

def è_palindromo(stringa):
    stringanuova=stringa.split()
    stringanuova1="".join(stringanuova)
    
    newstr=[]
    for i in stringanuova1:
        if i.isupper():
            newstr.append(i.lower())
        else:
            newstr.append(i)

    stringafinale=''.join(newstr)
    
    for j in range(len(stringafinale) // 2):  # Fino alla metà della stringa
        if stringafinale[j] != stringafinale[-(j + 1)]:  # Confronta avanti e indietro
            return False
    return True

stringa="A man a plan a canal Panama"
print(è_palindromo(stringa))


#senza ricorsione

# In[]

def è_palindromo(stringa):
    stringanuova=stringa.split()
    stringanuova1="".join(stringanuova)
    
    newstr=[]
    for i in stringanuova1:
        if i.isupper():
            newstr.append(i.lower())
        else:
            newstr.append(i)

    stringafinale=''.join(newstr)
    
    if len(stringafinale) <= 1:
        return True
    
    # Caso ricorsivo: confronta il primo e l'ultimo carattere
    if stringafinale[0] == stringafinale[-1]:
        return è_palindromo(stringafinale[1:-1])  # Ricorsione sulla sottostringa
    
    # Se i caratteri non corrispondono, non è un palindromo
    return False

stringa="A man a plan a canal Panama"
print(è_palindromo(stringa))

#con ricorsione

# In[]

def massimo(L):
    
    massimo_valore = L[0]
    
    for i in L:
        if type(i) == int:  # Se l'elemento è un numero intero
            if i > massimo_valore:
                massimo_valore = i
        elif type(i) == list:  # Se l'elemento è una lista
            massimo_sottolista = massimo(i)  # Chiama ricorsivamente la funzione per la sottolista
            if massimo_sottolista > massimo_valore:
                massimo_valore = massimo_sottolista
                
    return massimo_valore

L = [1, [2, 3], 4, [5, [6, 7]]]
print(massimo(L))  # Deve restituire 7

# In[]

def profondità(L):
    
    count = 0  # Inizializza il contatore una sola volta
    for i in L:
        if type(i) !=list:
            count += 1  # Aggiungi direttamente il valore intero
        else:
             profondità(i)
             count+=1
            
    return count


L = [1, [2, 3], [4, [5, [6]],5],8]
print(profondità(L))  # Deve restituire 3


#mia soluzione parzialmente giusta

# In[]

def profondità(L):
    # Se la lista è vuota, la profondità è 0
    if not L:
        return 0
    
    # Inizializza la profondità massima
    profondità_max = 0
    
    # Itera sugli elementi della lista
    for i in L:
        if type(i) == list:  # Se l'elemento è una lista, calcola la sua profondità
            profondità_max = max(profondità_max, 1 + profondità(i))  # Aggiungi 1 per il livello corrente
    
    return profondità_max

# Test
L = [1, [2, 3], [4, [5, [6]], 5], 8]
print(profondità(L))  # Deve restituire 3

# In[]

def profondità(L):
    
    ct=0
    for x in L:
        if type(x)==int:
            ct+=0
            
        else:
            ct=1+profondità(x)
        
    return ct        
L = [1, [2, 3], [4, [5, [6,[8]]], 5], 8]
print(profondità(L))

# In[]

def prodotto_lista(L):
    
    count = 1  # Inizializza il contatore una sola volta
    for i in L:
        if type(i) == int:
            count *= i  # Aggiungi direttamente il valore intero
        else:
            count *= prodotto_lista(i)  # Ricorsione sulla sottolista
    return count


L = [1, [2, 3], 4, [5, [6]]]
print(prodotto_lista(L))  # Deve restituire 720

# In[]

def concatena_stringhe(L):
    
    stringa=""
 
    stringa="".join(L)
    return stringa

L = ["Ciao","tutto"]
print(concatena_stringhe(L))  # Deve restituire "Ciaotutto"

#senza ricorsione

# In[]

def concatena_stringhe(L):
    
    # Caso base: se la lista è vuota, restituisci una stringa vuota
    if not L:
        return ""
    
    # Se l'elemento corrente è una lista, chiamala ricorsivamente
    if type(L[0]) == list:
        return concatena_stringhe(L[0]) + concatena_stringhe(L[1:])
    
    # Se l'elemento corrente è una stringa, aggiungila al risultato
    return L[0] + concatena_stringhe(L[1:])

L = ["Ciao", ["come", "va"], "tutto", ["bene"]]
print(concatena_stringhe(L))  # Deve restituire "Ciaotutto"

# In[]

def dec_to_bin(n):
    # Caso base: se n è 0, restituisci "0"
    if n == 0:
        return "0"
    
    # Caso base: se n è 1, restituisci "1"
    if n == 1:
        return "1"
    
    # Chiamata ricorsiva: divide il numero per 2 e restituisce il risultato
    return dec_to_bin(n // 2) + str(n % 2)

# Esempio di utilizzo
numero = 13
print(dec_to_bin(numero))
