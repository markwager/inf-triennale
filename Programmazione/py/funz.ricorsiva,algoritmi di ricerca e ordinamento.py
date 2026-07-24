#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:09:35 2024

@author: valerio
"""

def fib(n):
        """Assume n int >= 0
        Restituisce Fibonacci di n"""
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
def test_fib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        
test_fib(5)

#questa è una funzione ricorsiva ben definita: prima o poi convergerà
#Se si usa l’implementazione di fib, quante volte calcola il valore di fib(2) mentre si calcola fib(5)?

# In[]

def search(L, e):
    """Assume che L sia una lista.
       Restituisce True se e è in L,
           False altrimenti"""
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

L=[2,5,6,7,1]

print(search(L, 1))

#questa funzione ritorna True, ma si potrebbe restituire anche la posizione volendo mettendo i al posto di True
#il costo è di O(len(n)) sempre

# In[]

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
    return False

L=[1,2,3,4,4]

print(search(L, 1))

#in questo caso l'algoritmo è più efficiente perchè si fermerebbe nel caso di una lista ordinata.
#per esempio se dovessimo cercare il numero 3, questo si fermerebbe subito al raggiungimento del 3 nella lista
#l'algoritmo in questo caso costrebbe nel caso peggiore O(len(L))

# In[]

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

L=[1,2,3,4,5]

print(search(L, 6))

#questo programma consiste in due funzioni: una main e una annidata. La seconda possiede 4 parametri di cui, gli ultimi 2, sono
#da nascondere all'utente per ovvi motivi.
#low e high assumono in automatico rispettivamente il minimo e la lunghezza massima di L (vedi ultimo else)
#la funzione più interna richiama se stessa anzichè usare un ciclo while come lo ha usato il prof nella lezione 05.11.2024
#complessità temporale, spaziale: O(log(n)), O(log(n))

# In[]

def bubble_sort(a, key=None):
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
        
        #dal for fino all'if terminato c'è il main del bubble_sort che ordina
        #nel caso peggiore si ha un costo quadratico
        
def t1(e):
    return e[1] #posso switchare da 1 a 0 per la key per ordinare le lettere o i numeri

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
 
bubble_sort(a, key=t1)
print(a)

# In[]

#[algoritmo di fusione]
#questo algoritmo è il merge che confronta elemento per elemento tra le due liste per mettere poi gli elementi ordinati
#nella nuova lista

a=[0, 5, 8, 10, 11, 11, 14]
b=[1, 2, 6, 6, 6, 9 ,10]
c=[]

i, j=0, 0

while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

while i<len(a):
    c.append(a[i])
    i+=1

while j<len(b):
    c.append(b[j])
    j+=1
    
#i due ultimi while servono affinchè si possa completare la lista c perchè, una delle due condizioni, diventerà falsa e quindi i
#o j non scannerizzeranno tutta la loro corrispondente lista
print(c)

#complessità temporale: O(n)=len(a)+len(b)
# In[]

#il merge_sort è invece un algoritmo che divide, ordina e mette insieme. Usa l'algoritmo merge che, in questo caso, serve
#a ordinare la lista. Il merge_sort invece ha solo il compito di dividere la lista e poi di chiamare ricorsivamente se stessa
#e la funzione merge.
#La lista perciò si frammenta di mezzi in mezzi fino ad avere tante successioni quante sono gli elementi della lista, si
#confrontano tra loro, si riuniscono e si ha la lista di partenza ordinata.

def merge_sort(a, lx=0, rx=None): #non posso assegnare a un prametro il valore di un altro parametro
     
    if rx==None:
        rx=len(a)
    
    '''
    si può inserie una lista
    o una successione
    lx e rx (indice sx e dx)
    output: None
    effetto collaterale: ordinare in loco gli elementi di a[lx:rx] (cioè modificare la lista a)
    '''
    
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
        
        #quest'ultimo for copia gli elementi e di c nella lista a
    
    if lx+1 >= rx: #caso base
        return None
    
    cx=(lx+rx)//2
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    
    merge(a, lx, cx, rx)

a=[10, 21, 0, 30 ,34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge_sort(a)
print(a)

#complessità temporale: O(log(n)*n)
#complessità spaziale: funzioni ricorsive chiamate (log(n)) per via delle sottosuccessioni ordinate) + lista di appoggio c (O(n))
#ma effettivamente è O(log(n)+n)=O(n)

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
k = 12

print( ricerca_intervallo(a, k) )


#complessità temporale è n/2^i perchè si divide a potenze di 2---> 1=n/2^t----> O(log(n)) in base 2

# In[]

def ricerca_posizione(a, k):
    '''
    Input: a, una lista di numeri ordinati in modo crescente
           k, un numero da cercare
    Output: l'indice esatto del numero k se esiste nella lista;
            None altrimenti.
    '''
    lx, rx = 0, len(a) - 1

    while lx <= rx:
        cx = (lx + rx) // 2  # Calcolo dell'indice centrale
        if a[cx] == k:
            return cx  # Trovato l'indice esatto
        elif k < a[cx]:
            rx = cx - 1  # Cerca nella metà sinistra
        else:
            lx = cx + 1  # Cerca nella metà destra

    return None  # k non è nella lista

# Esempio di utilizzo
a = [-2, 3, 9, 12, 13]
k = 12

indice = ricerca_posizione(a, k)
print(indice)


# In[]
'''
Funzione di ricerca:
    complessità temporale: O(len(L))
    complessità spaziale: O(1)
    
Funzione di ricerca ricorsiva e binaria:
    complessità temporale: O(log(n)) dove n=len(L)
    complessità spaziale: O(log(n)) per via dello stack
    
Funzione ricerca binaria (funzione intervallo):
    complessità temporale: O(log(n))
    complessità spaziale: O(1)
    
Funzione merge (confronta elemento per elemento tra le due liste per mettere poi gli elementi ordinati nella nuova lista):
    complessità temporale: O(len(a)+len(b))
    complessità spaziale: O(1) perchè stampa il risultato
    
Funzione merge_sort (algoritmo che divide, ordina e mette insieme. Usa l'algoritmo merge che, in questo caso, serve
a ordinare la lista. Il merge_sort invece ha solo il compito di dividere la lista e poi di chiamare ricorsivamente se stessa
e la funzione merge):
    complessità temporale: O(log(n)*n)
    complessità spaziale: O(log(n)+n)=O(n) perchè stampa il risultato
'''


