#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:28:02 2024

@author: valerio
"""
#confronto tra sequenze (liste, tuple e stringhe)

print((1,2)<(1,2))
#print(('A',2)<(1,2))#questo genera un errore perchè non va bene confrontare stringhe con interi
print((1,2)<(1,2,5))#in questo caso vale True perchè la prima tupla è il prefisso dell'ultima
print((1,2)<(1,2,5))#in questo caso vale True perchè la prima tupla è il prefisso dell'ultima
print((1,2)<(1,1,5))#in questo caso vale False 
#si confronta una coppia per volta



# In[]

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
#voglio visualizzare le posizioni di questi punti
#non utilizzare memoria aggiuntiva, non modificare input
#non bisogna MAI modificare l'input (a meno che non sia specificato)
#determinare lx e rx (estremi nell'intervallo)
lx=a[0][1]
rx=a[0][1]
for e,p in a: #unpacking
    if p<lx:#tira fuori il min
        lx=p
        
    elif p>rx:#tira fuori il max
        rx=p
        
print(lx)
print(rx)
c=max(a) #in questo caso tira fuori la tupla e utilizza l'operatore '>' (gli interi non possono essere confrontati)
print(c)

# In[]
#oppure si usano max e min funzioni
#però facciamo noi la funzione max

def MAX(a, key=None): #key=None, valore di default, quindi se key==None massimizza e.
#Quindi il val None è messo come standard se l'utente non dovesse inserire il secondo valore, è in pratica una funzione
    '''
    input: a una lista, key una funzione
    output: e in a t.c key(e)=max(key(x) per x in a)
    '''
    
    def identity(e):
        return e
    
    if key==None:
        key=identity
        
        #si sta dicendo che se la seconda funzione è nulla, quindi non immessa dall'utente, la funzione key = a quella sopra
        
    r_max=key(a[1]) #restituisce un valore fissato arbitrariamente da noi (può essere 0,1...); in questo caso -2
    for e in a:
        if key(e)>r_max:
            r_max=key(e)
    return r_max

def t1(e):
   return e[1] #restituisce il secondo elemento degli elementi di a

#questo def lo metterei tra r_max e for perchè secondo me ha più senso perchè key(e) cambia leggendo ogni elemento della tupla 
#(le liste) e poi la funzione prende il secondo elemento delle liste e nel for si confrontano i valori (stessa cosa succede con r_max)


a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
print(MAX(a, key=t1)) #ritorna il valore massimo confrontando tutti i valori interi grazie a key (confronta gli elementi al secondo indice)
print(MAX(a))

# In[]

def MAX(a, key=None): #key=None, valore di default, quindi se key==None massimizza e.
#Quindi il val None è messo come standard se l'utente non dovesse inserire il secondo valore
    '''
    input: a una lista, key una funzione
    output: e in a t.c key(e)=max(x) per x in a
    '''
    def identity(e):
        return e
    
    if key==None:
        key=identity
        
    v_max=key(a[0])
    r_max=a[0]
    
    for e in a:
        if key(e)>v_max:
            v_max, r_max=key(e), e
    return r_max

def t1(e):
    return e[1]

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
print(MAX(a, key=t1)) #ritorna la tupla con il valore massimo

# In[]

#il parametro key delle fun<ioni min e max è lo stesso della funzione MAX
print(max(a,key=t1))

# In[]
    
def t1(e):
    return e[1]

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]

lx=min(a, key=t1)[1]
rx=max(a, key=t1)[1]
#questi trovano primi i massimi numeri interi tra liste nella tupla, prendendo la lista col numero max e identificando solo l'int

for p in range(lx, rx+1): #possiamo introdurre un altro parametro
    c='*'
    for e, v in a:
        if p==v:
            c=e
    print(c, end='') #non utilizzo una nuova stringa vuota da riempire per evitare memoria supplementare
print('\nfine')

# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]

    lx=min(a, key=t1)[1]
    rx=max(a, key=t1)[1]
   
    for p in range(lx, rx+1): #possiamo introdurre un altro parametro
        c='*'
        for e, v in a:
            if p==v:
                c=e
        print(c, end='') #non utilizzo una nuova stringa vuota da riempire per evitare memoria supplementare, O(1) perchè c è un char
    print('\nfine')

#complessità temporale  m=rx-lx --> O(n*m) dove n=len(a) il costo è quindi almeno quadratico
#complessità spaziale O(1) perchè non c'è spazio supplementare
    
a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
print(disegna_punti_su_retta(a))

# In[si può ridurre la complessità temporale a scapito di quella spaziale?]




    
    
            



