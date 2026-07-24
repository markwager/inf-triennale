#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:07:30 2024

@author: valerio
"""

def del_item(a,v):#a è un parametro formale
#a una lista, v è un valore, return None. Elimina da a le occorrenze di v
    i=0
    n=len(a)
    while i<n:
        if a[i]==v:
            del (a[i]) #O(n)
            n-=1
        else:
            i+=1
L=[1,2,3,4,6]#variabile globale
print(del_item(L, 2))
print(L)

#questa funzione ha complessità temporale quadratica (O(n^2))

#gli ambienti sono specifiche delle funzioni: contengono i dati necessari per avviare le funzioni (o frame)
#l'ambiente della funzione contiene i parametri formali e le variabili locali
#ci sono due ambienti: quello della funzione e quello esterno (programma principale)
#L diventerà un alias di a grazie alla funzione
#tutte le varibaili interne alla funzione sono quelle locali e poi vengono butatte via
#se non è specificato il return nella funzione, restituisce sempre il valore None
#complessità spaziale: O(1) per via di i=0

# In[]

def f(x):
    a=x+[0]*g(x)
    print(a)
    return len(a)
    
def g(x):
    n=int(input('Digita un numero: '))
    return n

L=[0,1,2]
n=f(L)
print(n)

# In[]

def del_item(a,v):
#a una lista, v è un valore, return None. Elimina da a le occorrenze di v
    b=[]
    
    for x in a:
        if x!=v:
            b.append(x)
    return b #alias di b

L=[1,2,3,4,6]
print(del_item(L, 2))

#non è corretta perchè non modifica a (si usa b invece) e poi non restituisce None


#non è considerata una soluzione valida perchè non ripsetta le specifiche, ma è più efficiente
#b sopravvive perchè L diventerà un alias della nuova lista (b), ma può fare l'alias non contemporaneamente prima all'oggetto
#specificato dall'utente e poi alla nuova lista finale

# In[]


def del_item(a,v):
#a una lista, v è un valore, return None. Elimina da a le occorrenze di v
    b=[]
    
    for x in a:
        if x!=v:
            b.append(x)
    a=b #alias di b

L=[1,2,3,4,6]
print(del_item(L, 2))

#non va bene perchè la lista nuova è appesa a vuoto e non collegata a nulla
# In[versione migliorata]

def del_item(a,v):
#a una lista, v è un valore, return None. Elimina da a le occorrenze di v
    b=[]
    
    for x in a:
        if x!=v:
            b.append(x)
    
    i=0
    while i<len(b):
        a[i]=b[i]
        i+=1
    while i<len(a):
        del(a[i])

L=[1,2,3,4,6]
print(del_item(L, 2))
print(L)

#soluzione corretta, ma ancora non eficiente l'ultimo while ha costo quadratico nel caso peggiore

# In[]

def del_item(a,v):
#a una lista, v è un valore, return None. Elimina da a le occorrenze di v
    b=[] #cresce linearmente con la dimensione dell'input, quindi efficienza temporale ma non spaziale in confronto al primo codice
    
    for x in a:
        if x!=v:
            b.append(x)
    
    i=0
    while i<len(b):
        a[i]=b[i]
        i+=1
    while i<len(a):
        del(a[-1])

L=[1,2,3,4,6]
print(del_item(L, 2))
print(L)

#ora il costo dell'ultimpo while è lineare: complessità temporale O(n)
#quindi il primo codice aveva un costo quadratico e abbimao fatto un po' di tentativi per poi arrivare infine qua
#se volessimo esprimere il costo di memoria come quello temporale, si può fare
#possiamo solo ottimizzare lo spazio supplementare: cioè le variabili locali
#non possiamo ottimizzare l'input
#complessità spaziale: O(n) per via della grandezza di b=[]


