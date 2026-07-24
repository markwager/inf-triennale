#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:12:00 2024

@author: valerio
"""


#dati dei punti ordinati su una retta e un input k, si deve determinare a quale segmento k appartiene
#si può pensare a una ricerca lineare, ma è meglio una binaria perchè è più efficiente

#trovare un certo intervallo cx in a t.c. a[cx]<=k<a[cx+1] (non può essere chiuso anche a dx altrimenti apparterrebbe a due punti)


a=[-2,3,9,12,13]
k=9

lx,rx=0,len(a)-1

while lx<=rx:
    cx=lx+rx//2 #arrotondamento per difetto
    if k==a[cx]:
        print(a[cx], a[cx+1]) #perchè l'intervallo è chiuso a sx e aperto a dx
        break
    elif k<a[cx]:
        rx=cx-1
    else:
        lx=cx+1

if k<a[cx]:
    print(a[cx-1],a[cx])
elif k>a[cx]:
    print(a[cx],a[cx+1])
        
# In[]
def ricerca_intervallo(a, k):
    '''
    Input: a, una lista di numeri ordinati in modo crescente, valori consecutivi
        in a rappresentano un intervallo chiuso a sinistra e aperto a destra;
        k, un numero
    Output: se k>=a[0] e k < a[-1], una coppia (a[i], a[i+1]) che rappresenta
        l'intervallo contenente k; se k < a[0] la funzione ritorna ('-inf', a[0]);
        se k >= a[-1] la funzione ritorna (a[-1], '+inf')
    '''
    lx, rx = 0, len(a)-1
    
    if k < a[0]:
        return ('-inf', a[0])
    
    if k >= a[-1]:
        return (a[-1], '+inf')
    
    while lx <= rx:
        cx = int( (lx+rx)/2 )
        if k == a[cx]:
            return ( a[cx], a[cx+1])
        elif k < a[cx]:
            rx = cx-1
        else:
            lx = cx+1
     
    if k < a[cx]:
        return ( a[cx-1], a[cx]) 
    elif k > a[cx]:
        return ( a[cx], a[cx+1] )
    

# complessità spaziale: O(1)
# complessità temporale: O(log_2 n)
    
a = [-2, 3, 9, 12, 13]
k = 10

print( ricerca_intervallo(a, k) )


#complessità temporale è n/2^i perchè si divide a potenze di 2---> 1=n/2^t----> O(log(n)) in base 2