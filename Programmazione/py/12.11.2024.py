#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:53:06 2024

@author: valerio
"""

#in pratica si confrontano strignhe nel loro ordine lessico-grafico

def merge_sort(a, lx=0, rx=None):
     
    if rx==None:
        rx=len(a)
        
    def merge(a, lx, cx, rx):

        c=[]

        i, j=lx, cx

        while i<cx and j<rx:
            if a[i]<a[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(a[j])
                j+=1

        while i<cx:
            c.append(a[i])
            i+=1
            
        while j<rx:
            c.append(a[j])
            j+=1
            
        i=lx
        for e in c:
            a[i]=e
            i+=1
    
    if lx+1 >= rx: #caso base
        return None
    
    cx=(lx+rx)//2
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    
    merge(a, lx, cx, rx)
    
a=[10, 21, 0, 30 ,34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge_sort(a)
print(a)


a=['programmazione', 'del', 'cazzo']
merge_sort(a)
print(a)

# In[funzione lambda]

v=(lambda x: x**2)(2) #v è il valore della funzione. c'è un parametro e un input

f=lambda x:x #è una funzione

# In[]

#e se voglio ordinare per lunghezza? Cioè dalla più corta alla più lunga?

def merge_sort( a, key = lambda x:x, lx = 0, rx = None ):
    
    def merge(a, lx, cx, rx):

        i, j = lx, cx
        c = []
        while i < cx and j < rx:
            if key(a[i]) <= key(a[j]):
                c.append(a[i])
                i += 1
            else:
                c.append(a[j])
                j += 1
        
        while i < cx:
            c.append(a[i])
            i+=1
            
        while j < rx:
            c.append(a[j])
            j += 1
            
        i = lx
        for e in c:
            a[i] = e
            i += 1
    
    if rx == None:
        rx = len(a)
    
    if lx+1 >= rx:
        return None
    
    cx = int((lx+rx)/2)
    
    merge_sort(a, key, lx, cx)
    merge_sort(a, key, cx, rx)
    merge(a, lx, cx, rx)

a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort(a, key=len)
print(a)

# In[metto prima i numeri e poi le stringhe]

a=['programmazione', 'del', 'cazzo', 56, 132.6, 90]

def f(x):
    if type(x) in (int,float):
        return 0
    else:
        return 1
    
merge_sort(a, key=f)

print(a)

merge_sort(a, key=lambda x: 0 if type(x) in (float, int) else 1)

print(a)

# In[]

#voglio mettere prima i numeri e poi le stringhe e ordinarli 

def f(x):
    if type(x) in (int, float):
        return (0,x)
    elif type(x) == str:
        return (1, x)
    
a=['programmazione', 'del', 'cazzo', 56, 132.6, 90]
merge_sort(a, key=f)
print(a)

# In[]

#voglio mettere prima i numeri e poi le stringhe e ordinarli, ordinare per lunghezza le stringhe

def f(x):
    if type(x) in (int, float):
        return (0,x)
    elif type(x) == str:
        return (1, len(x))
    
a=['programmazione', 'del', 'cazzo', 56, 132.6, 90]
merge_sort(a, key=f)
print(a)

#inoltre, non potrà mai accadere che si fanno ocnfronti tra numeri e stringhe: perchè si confronta sin da subito il parametro (1 o 0)
#per capire se si ha un numero o una stringa

# In[funzione sorted]
#prende in input un iterabile: un qualsiasi tipo di dato su cui è possibile iterare (lista, tupla, stringa)
a=(10,9,11,0,4)
print(sorted(a))
#se gli do inpasto una tupla, mi restituisce una lista
#crea un nuovo oggetto
#ha la stessa complessità

# In[metodo sort]

#un metodo è una specie di funzione utilizzato solo per determinati tipi di dato. Quindi sort è un metodo della classe lista
#il metodo sort applica una modifica in loco

a=[10,9,11,0,4]
a.sort()
print(a)

