#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:09:08 2024

@author: valerio
"""

def search(L, e):
    """Assume che L sia una lista.
       Restituisce True se e è in L,
           False altrimenti"""
           
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

#complessità temporale: sempre O(len(L))

L=[1,2,3,4,5]
print(search(L, 9))




# In[ricerca efficiente]

def search(L, e):
    """Assume che L sia una lista, i cui elementi
           sono ordinati in ordine crescente.
       Restituisce True se e è in L,
           False altrimenti"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
        
#questo è un algoritmo di ricerca che ottimizza la complessità temporale nel migliore dei casi, ma O(len(L)) resta sempre
#nel peggiore dei casi.
#cioè si ottimizza il tempo medio nel caso di una lista ordinata in ordine crescente di numeri interi

L=[1,2,3,4,5]
print(search(L, 6))

# In[ricerca binaria]

def search(L, e):
    """Assume che L sia una lista, i cui elementi
           sono ordinati, in ordine crescente.
       Restituisce True se e è in L,
           False altrimenti"""

    def bin_search(L, e, low, high):
        #Decrementa high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #non resta nulla in cui cercare
                return False
            else:
                return bin_search(L, e, low, mid - 1)
        else:
            return bin_search(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)

# In[]

def mult(arg1, arg2=None):
    if arg2!=None:
        return (arg1*arg2)
    else:
        return (arg1)


print(mult(4))

# In[]

#Scrivere un'espressione lambda che abbia due parametri numerici. Se il secondo argomento è uguale a zero,
#deve restituire None; altrimenti deve restituire il valore della divisione del primo argomento per il secondo.
#Suggerimento: usate un'espressione condizionale.

x= lambda a,b: None if b>a else a/b
print(x(2,2))

# In[]

#Si scriva una funzione che abbia tre parametri obbligatori (x, y e z) ed un parametro facoltativo (key)
#che sia una funzione che assegni a x, y e z un valore. La funzione restituisca il massimo tra x, y e z rispetto alla funzione
#key. Il valore predefinito per key sia la funzione identità.

def find_max(x,y,z, key=None):
    if key==None:
        if x>y and x>z:
            return x
        elif y>x and y>z:
            return y
        else:
            return z
    elif key!=None:
        if key(x)>key(y) and key(x)>key(z):
            return x
        elif key(y)>key(x) and key(y)>key(z):
            return y
        else:
            return z
    
print(find_max('affffffs', 'b', 'cdfa', key=len))
    
# In[]
#La somma armonica di un intero, n > 0, si può calcolare con la formula
#1 + 1/2 + 1/3 + ... + 1/n
#Scrivete una funzione ricorsiva che la calcoli.

def arm_sum(n):
    if n==1:
        return 1
    else:
        return 1/n + arm_sum(n-1)
        
n=3
print(arm_sum(n))       

# In[]

'''
    Precondizione: t è una tupla che può contenere al suo interno
        tuple annidate
    Restituisce il numero di elementi numerici contenuti in t
        ed in tutte le tuple annidate
'''

def deep_count(a):
    
    b = 0
    for e in a:
        if type(e) != tuple:
            b+=1
        else:
            b+=(deep_count(e))
    return b

a = ( 1, (0, 3.14, 0), 100, (2, 5) )
b = deep_count(a)
print(b)

# In[]

#Scrivere una funzione Python denominata deep_copy che cloni la lista in input e tutte le liste annidate che essa contiene

def deep_copy(a):
    
    b = []
    for e in a:
        if type(e) != list:
            b.append(e)
        else:
            b.append(deep_copy(e))
    return b

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]
b = deep_copy(a)
print(b)
print(id(b)==id(a))
#si ha un id diverso se si ha una copia delle variabili
#se l'id è uguale, allora si ha un alias

# In[]

#Scrivere una funzione che stampi tutte le permutazioni di una lista in input

def permuta( a, i  = 0):
    if i < len(a):
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            permuta(a, i+1)
            a[i], a[j] = a[j], a[i]
    else:
        print(a)
        
a = [ 'python', [0, 3.14, '2.71']]
b=permuta(a)

#praticamente la funzione, con la ricorsione, torna indietro in automatico

# In[]

#Sia a una lista di n interi maggiori o uguali a 0, si scriva una funzione, denominata combinazioni che stampi tutte le liste
#b di interi maggiori o uguali a zero e di lunghezza n tali che b[i] < a[i] per ogni i = 0,..., n-1.

#Ad esempio se a = [3, 1, 2], la funzione stamperebbe

'''
[0, 0, 0]
[0, 0, 1]
[1, 0, 0]
[1, 0, 1]
[2, 0, 0]
[2, 0, 1]
'''

def combinazioni( a ):
    def comb_rec(a, b, i = 0):
        if i == len(a):
            print(b)
        else:
            for x in range(a[i]):
                b[i] = x
                comb_rec(a, b, i+1)
    b = [0]*len(a)
    comb_rec(a, b)
    
a=[3, 1, 2]
combinazioni(a)

# In[]












