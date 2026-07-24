#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:20:44 2024

@author: valerio
"""

#continuo dell'esercizio di ieri mattina

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]

    lx=min(a, key=t1)[1]
    rx=max(a, key=t1)[1]
    m=rx-lx+1
    retta=['*']*m #O(m) tempo e spazio
    
    for e, p in a: #tempo O(n)
        retta[p-lx]=e
    print(''.join(retta)) #tempo O(m)
    
a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
print(disegna_punti_su_retta(a))

#complessità temporale O(n+m) e spaziale O(m)
#non è migliorabile la complessità spaziale perchè devo comunque leggere l'input
# In[ordinamento]

a=[6, 1, 9, 0, -4, 5, 8 ,10, 4]

#bubblesort

n=len(a)
for c in range(n-1):
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i], a[i+1]=a[i+1], a[i]
print(a)

#complessità temporale è O(n^2) sempre

# In[]

a=[6,1, 9, 0 ,-4, 5, 8 ,10, 4]

#bubblesort

n=len(a)
for c in range(n-1):
    for i in range(n-1-c): #perchè così stoppo l'algoritmo prima se degli elementi sono già ordinati
        if a[i]>a[i+1]:
            a[i], a[i+1]=a[i+1], a[i]
print(a)

#il costo resta sempre quadratico anche migliorandolo di poco

# In[]

a=[6, 1, 9, 0 ,-4, 5, 8 ,10, 4]
#bubblesort
#l'idea: se in una scansione non si effettuano scambi, la lista è ordinata

n=len(a)
for c in range(n-1):
    terminato=True
    for i in range(n-1-c): #perchè così stoppo l'algoritmo prima se degli elementi sono già ordinati
        if a[i]>a[i+1]:
            a[i], a[i+1]=a[i+1], a[i]
            terminato=False
    if terminato==True:
        break
#complessità temporale O(n^2) nel caso peggiore
print(a)

# In[]

def t1(e):
    return e[1]

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]

n=len(a)

for c in range(n-1):
    terminato=True
    for i in range(n-1-c): #perchè così stoppo l'algoritmo prima se degli elementi sono già ordinati
        if t1(a[i])>t1(a[i+1]):
            a[i], a[i+1]=a[i+1], a[i]
            terminato=False
    if terminato==True:
        break

print(a)

# In[]
def bubble_sort(a, key =None):
    def identity(e):
        return e
    n=len(a)
    
    if key==None:
        key=identity
    
    for c in range(n-1):
        terminato=True
        for i in range(n-1-c): #perchè così stoppo l'algoritmo prima se degli elementi sono già ordinati
            if key(a[i])>key(a[i+1]):
                a[i], a[i+1]=a[i+1], a[i]
                terminato=False
        if terminato==True:
            break
def t1(e):
    return e[1]
 
a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
 
bubble_sort(a, key=t1)
print(a)

# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    n=len(a)
    #m=rx-lx
    b=a[:]
    bubble_sort(b, key=t1) #Tempo O(n^2) e spazio O(n)
    lx, rx=b[0][1], b[-1][1]
    i=0 #indice in b del prossimo punto da stampare
    for p in range(lx, rx+1):
        if i<n and p==b[i][1]:
            print([b[i][0]], end='')
            i+=1
        else:
            print('*', end='')
            
a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
disegna_punti_su_retta(a)

#complessità: O(n^2+m) nel caso peggiore
#spazio O(n)
