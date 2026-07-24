#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:05:12 2024

@author: valerio
"""

# In[]

#Sia T(n)=2n^2+n/4+9, allora T(n) appartiene a O(n^2) oppurea O(n^3) perchè si parla di limitazione superiore
#Si parla di theta(n^2) se è proprio n^2
#bisogna ragionare sempre nel caso peggiore nel caso in cui bisogna calcolare il costo della funzione (questo per semplificare il l'analisi di costo di una funzione)
#def O(): T(n) appartiene a O(f(n)) ---> T(n)<=f(n) cioè T(n) cresce di meno di f(n) ---> T(n)<=cf(n) se n>=n0 con n0,c costanti
#Es: T(n)=6n+4 appartiene a O(n) perchè c potrebbe essere 40 e, quindi, 6n+4<=cn ---> 6n+4<=40n per n>=n0
#se trovo anche T(n)>=c'n per n>=n0' allora ottengo un Theta

# In[]

a='programmazione'
#a[0]= 'P'
#le stringhe sono immutabili!
a='P'+a[1:] #mo funziona
print(a)

# In[]

#assegnazione multipla

a,b= 10,11
t=10,2,3 #è legale
print(t)
print(type(t)) #t è una tupla: una sequenza di elementi di qualsiasi tipo
t=(0,'str',(1,2,3), 3.14)
print(t)
print(len(t))
#4 elementi
print(t[2])
print(t[0:2])
print(t[::-1])
#lo slicing crea sempre delle copie
print(2*t)
print(t+(1,2))
for x in t:
    print(x)
#la tupla è immutabile, cioè non posso fare t[1]=0 non posso

t=('a','b','c')
x,y,z=t #spacchettamento (unpacking=num delle varibaili=numero di elementi della tupla)
t=x,y,z #impacchettamento (packing)
# In[]

#la lista è come una tupla, ma mutabile
a=[0,'stringa',(1,2)]
a[0]='sas'
print(a)
del(a[1])
print(a)
#si sta solo modificando la lista, non ne crei una nuova

# In[]

a=[]

a.append(100)
a.append(200)
print(a)

a=a.append(70) #attenzione, append non ha il return. Questo metodo (perchè si applica solo alle liste, funzione speciale aggiunge in coda)
print(a)

# In[]

a=[('A', 2, 7), ('B', 3, -1), ('C', 0 ,1), ('D', -2, -2)]
r=2.9
#n=len(a)
#crea una lista che contiene i nomi dei punti in a a distanza al più r da (0,0,0)
b=[]
print(type(a))

for n,x,y in a: #unpacking
    if x**2+y**2<=r**2:
        b.append(n) #O(1) cioè è costante in media
print(b)
        
#complessità temporale: per il metodo append, n operazioni con append danno un costo lineare ---> O(n)
##proprietà: n append consecuitivi costano complessivamente O(n) nel caso peggiore
#quindi l'algoritmo ha comlessità temporale O(n) nel caso peggiore



    

