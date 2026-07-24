#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:02:06 2024

@author: valerio
"""

a='ciaogioygoy'
n=len(a)
print(a[-1])
print(a[:-3])#stampa i caratteri di ciao da sx verso dx (se parti da -3 stampa c)
print(a[-1:])#stampa i caratteri di ciao da dx verso sx (se parti da -1 stampa 0)
print(a[1:-1])
print(a[::-1])#stampa al contrario i caratteri
print(a[1:3])
print(len(a[1:-1]))

# In[]

n, flag = 0, True
while flag:
    x = input('Scrivi qualcosa: ')
    if len(x) < n:
        flag = False
    n = n+1

# In[]

def f(x, y=2):
    return x*y+x

print(f(2))

#y può essere aggiornato, quindi puoi mettere qualsiasi y dentro la funzione

# In[]

a = [(4, 'quattro'), 6, (3, 1, 2), 6, 1 ]
print(a[-1])
somma=0

for x in a:
    if type(x) != int:
        somma += x[0] #si accede al primo elemento della tupla se non si ha un intero
    else:
        somma += x
        
print(somma)

# In[]

n=2

a = list(range(n))

print(a)

# In[]

a = []
for i in range(n):
    a.append(str(i))

b = a;

d = {}

for x in a:
    d[x] = b[int(x)]
print(d)
print(len(d))

# In[]
x=[1,2,3]
d = {}
k=17
for i in x:
    d[i] = i
    
print(d)

# In[]
a=[1,2,3]
d = {}
k=17
for i in a:
    d[i] = i*'x'

print(d)

print(d.get(1)) #stampa il valore associato alla chiave 1
print(d.get(1,3))#stampa il valore associato alla chiave 1 ignorando 3
print(d.get(4,3))#stampa il 3 dato che non c'è la chiave 4

# In[]

a=[0,1]
b=[1,0]
x=zip(a,b)
print(tuple(x))

# In[]
n=2

a = list(range(n))
b = a[::-1]
s = 0
for x in zip(a, b):
    s += x[0]+x[1]
    print(tuple(zip(a,b)))

print(s)

# In[]

a=(1,2,3)
b=a[0]
print(b)

# In[]

a='ciao'
print(a[0:-1])
