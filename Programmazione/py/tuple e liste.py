#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:35:06 2024

@author: valerio
"""

#Le tuple sono sequenze ordinate e immutabili di elementi (come le stringhe). La differenza è che gli elementi di una tupla non devono essere per forza caratteri.
#I singoli elementi possono essere di qualsiasi tipo e in una stessa tupla non devono neanche essere tutti dello stesso tipo.

t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)
print(3*t2)
# In[]
#Come alle stringhe, anche alle tuple si possono applicare concatenazione, indicizzazione e slicing. Per esempio,

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2))
print((t1 + t2)[3])
print((t1 + t2)[2:5])

# In[]

def intersect(t1, t2):
    """Assume che t1 e t2 siano tuple
       Restituisce una tupla che contiene gli elementi
          che sono sia in t1 sia in t2 """
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result
print(intersect((1, 'a', 2), ('b', 2, 'a')))

# In[]

# Scrivete un’espressione il cui valore sia la media di una tupla di numeri. Usate la funzione sum.
a=(1,2,3,4,5,6)
for x in a:
    print(x) #questa è una cosa a parte

print(sum(a)/len(a))

# In[]

#Come una tupla, una lista è una sequenza ordinata di valori ognuno dei quali è identificato da un indice
#le liste sono iterabili
L = ['I did it all', 4, 'love']
for e in L:
    print(e)
    
    
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print('Univs =', Univs)
print('Univs1 =', Univs1)
print(Univs == Univs1)

print(Univs == Univs1) #testa l'uguaglianza tra valori
print(id(Univs) == id(Univs1)) #verifica l'uguaglianza tra
                               #oggetti
print(Univs is Univs1) #verifica l'uguaglianza tra oggetti
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))

# In[]

L1 = [[]]*2 #due elementi con lo stesso oggetto
L2 = [[], []]#due elementi con due diversi oggetti
for i in range(len(L1)):
    L1[i].append(i)
    L2[i].append(i)
print('L1 =', L1, 'ma', 'L2 =', L2)

# In[]

L = [1, 2, 3]
L.append(L)
print(L)
print(L is L[-1])

# In[]

#clonazione
def remove_dups(L1, L2):
    """Assume che L1 e L2 sono liste.
       Elimina da L1 qualsiasi elemento
           che sia presente anche in L2"""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)
#questo codice creerebbe una nuova lista eliminando da L1 gli elementi in comune con L2. Spoiler: non funziona

# In[versione corretta]

#clonazione
def remove_dups(L1, L2):
    """Assume che L1 e L2 sono liste.
       Elimina da L1 qualsiasi elemento
           che sia presente anche in L2"""
    for e1 in L1[:]:  #ora funziona, ma con lo slicing (uguale alla funzione copy)
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)

# In[]

def f(L1, L2):
    """L1, L2 sono liste di numeri della stessa
        lunghezza
    restituisce la somma degli elementi di L1
        elevati alla potenza dell'elemento allo stesso
        indice in L2
        Per esempio, f([1, 2], [2, 3]) restituisce 9"""
    L3=0
    for i in range(len(L1)):
        L3+=L1[i]**L2[i]
    return L3

print(f([3,2,1],[2,2,1]))

# In[]




