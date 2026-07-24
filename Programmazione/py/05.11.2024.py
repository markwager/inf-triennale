#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:18:38 2024

@author: valerio
"""

#In [esercizio]
#ho una sequenza di numeri ordinati in una lista, trovare la posizione dell'occorrenza più a dx di k di a
#es: l'algoritmo ritorna 5, altrimenti ritorna -1

def ricerca_intervallo(a, k):

    lx, rx = 0, len(a)-1
    
    while lx <= rx:
        cx = int((lx+rx)/2)
        if k == a[cx] and (cx == len(a)-1 or a[cx+1]>k):
            return (cx)
        elif k<a[cx]:
            rx=cx-1
        else:
            lx = cx+1
    
    if k!=a[cx]:
        return -1
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=19

print(ricerca_intervallo(a,k))

# In[]

a=[1,5,7,7,7,9,9,10,13,13,14,17]

c=a #c è un alias

b=a[:]

print(id(a)==id(b))
print(id(a)==id(c))

# In[]

a=['python', [0, 3.14, '2.71'], 100, ['programmazione', 'python']]
b=a[:] #si copia solo il primo livello, è una copia superficiale. Le liste annidate sono alias

a[1][0]='uno'
a[0]=2014 #va a risparmio di memoria e di tempo, quindi non si modifica in realtà

print(b)
# In[come clonare ai livelli successivi?]

a=['python', [0, 3.14, '2.71'], 100, ['programmazione', 'python']]

b=[] #in b ci va l'alias di a

for x in a:
    b.append(x)
    
print(b)

# In[]

a=['python', [0, 3.14, '2.71'], 100, ['programmazione', 'python']]

b=[] #in b ci va la copia di a

for x in a:
    if type(x)==list:
        b.append(x[:])
    else:
        b.append(x)
        
a[1][0]='uno'
a[0]=2014
    
print(b)

#si crea un altro alias al livello successuvo

# In[]

#si usa la ricorsione: tecnica che consente di risolvere un problema su una istanza risolvendolo sulle sotto-istanze
#una funzione che nvoca se stessa in pratica

#ho una prima lista di numeri qualsiasi, trovare il massimo nella lista
#max(a)= x app. ad a t.c per ogni e app. a, e<=x
#max(a)={a[0] se len(a)=1
       #{max(a[0], max(a[1:])) se len(a)>1
#in questo modo si usa la ricorsione. La funzione è poi ben definita: ha bisogno di convergere 

def r_max(a):
    if len(a)==1:
        return a[0]
    else:
        m=r_max(a[1:])
        if m>a[0]:
            return m
        else:
            return a[0]
    
        
a= [5,1,2,7,8,2,1]
print(r_max(a))

#complessità temporale: n=len(a)
#sia T(n) il numero di passi eseguita da r_max() su input di dim n

#se T(1)=O(1)
#altrimenti, siano c e d due costanti e T(n-1) è il costo della funzione richiamata
#T(n)=c+d(n-1)+T(n-1)=c+d(n-1)+c+d(n-2)+T(n-2)=2c+d(n-1)+d(n-2)+c+d(n-3)+T(n-3)=3c+d(n-1+n-2+n-3)+T(n-4)=......
#=kc+d((n-1)+(n-2)+...+(n-k))+T(n-k)= ... = (n-1)c+d(n-1+(n-2)+..+(1))+T(1)=
#(n-1)c + dn(n-1)/2 + O(1)
#O(n^2) per via dello slicing che lo utilizziamo n-1 volte
#complessità spaziale: O(n^2) per via dello slicing 

# In[]

def r_max(a,i=0):
    if i==len(a)-1:
        return a[i]
    else:
        m=r_max(a, i+1)
        if m>a[i]:
            return m
        else:
            return a[i]
    
        
a= [5,1,2,7,8,2,1]
print(r_max(a))

#funzione che evita lo slicing
#complessità temporale: O(n) perchè saprisce la parte d del costo del programma precedente
#complessità spaziale: bisogna contare i frame. In questo caso O(n) per via del numero di elementi nell lista
#complessità spaziale fa schifo

# In[]

a=['python', [0, 3.14, '2.71'], 100, ['programmazione', 'python']]

b=[] #in b ci va la copia di a

for x in a:
    if type(x)==list:
        b.append(x[:])
    else:
        b.append(x)
        
a[1][0]='uno'
a[0]=2014
    
print(b)