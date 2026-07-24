# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:26:54 2024

@author: Ginevra
"""

# In[1]
# per quali valori di condizione0 e condizione1 la funzione restiruisce True ? 

condizione0 = False
condizione1 = False
def f(condizione0, condizione1) : 
    if condizione0 and not condizione1 :
        return condizione1
    elif condizione1 :
        return False
    else : 
        return True
print(f(condizione0, condizione1))  

# risposte :
# A : True, True
# B : True, False
# C : False, True
# D : False, False 

# se condizione0 = True e condizione1 = True, stampa il secondo return con condizione1 False
# se condizione0 = True e condizione1 = False, stampa il primo return con condizione1 False
# se condizione0 = False e condizione1 = True, stampa il secondo return con condizione1 False
# se condizione0 = False e condizione1 = False, stampa il terzo return con condizione1 True

# risposta corretta : D
    
    
# In[2]
# sia n un intero positivo, quale è il valore di i+j al termine del seguente frammento di codice ?

n = input('scrivi un intero positivo: ')
i , j = 0, 2*n 
while i < j : 
    i += 1
    j -= 1

# risposte :
# A : 2n-1
# B : 0
# C : n-1
# D : 2n
# E : n 

# io so che il while continua fino a quando la condizione è vera e termina nel momento in cui diventa falsa
# il solo intero positivo per cui questa condizione può essere falsa è lo zero 
# quindi se i = 0 e j = 2*n, allora i+j = 2*n

# risposta corretta : D

    

# In[3]
# sia k un intero positivo, cosa viene stampato dal seguente frammento di codice ? 

k = input('scrivi un intero positivo: ')
n = 2*k+1
a , b = n/2 , n/2
print(int(a)+int(b) < int(a+b))

# risposte : 
# A : False
# B : 0
# C : n
# D : True
# E : una stringa

# è un confronto, quindi stamperà o true o false
# per k = 1 io so che n = 3
# a , b = 3/2 , 3/2 
# 3/2 è 1,5 quindi il suo intero è 1
# mentre 3/2 + 3/2 = 6/2 = 3
# mi sta chiedendo se 2 < 3

# risposta corretta : D

    

# In[4]
# sia L una lista di n scalari : quale è la complessità temporale e spaziale di m(L) ? 

def m(a) :
    if a[0] > max(a[1:]) :
        return a[0]
    else : 
        return max(a[1:])

# risposte : 
# A : Theta(n) tempo e Theta(n) spazio
# B : Theta(n) tempo e O(1) spazio
# C : Theta(n*n) tempo e O(1) spazio
# D : O(1) tempo e O(1) spazio
# E : Theta(n*n) tempo e Theta(n) spazio

# quello su cui mi devo concentrare è il primo for che contiene una cosa costosa come lo slicing ch eva da 1 a n-1 incluso
# lo slicing mette a confronto delle parti di lista e inoltre ne crea una nuova 
# però lo slicing è esattament euna funzione lineare in quanto limitata sia inferiormente che superiormente

# risposta corretta : A / E 

    

# In[5]
# si consideri il seguente frammento di codice. per quali tipi di a, b, c il valore di x non è definito ?

# x = a*b+c
# print(x)

# risposte : 
# A : type(a) == int, type(b) == str, type(c) == str
# B : type(a) == int, type(b) == tuple, type(c) == tuple
# C : type(a) == tuple, type(b) == int, type(c) == tuple
# D : type(a) == float, type(b) == int, type(c) == int
# E : type(a) == int, type(b) == int, type(c) == tuple
# F : type(a) == str, type(b) == int, type(c) == str

# posso sempre moltiplicare un intero per una stringa e viceversa , mi da una stringa che posso concatenare a str
# posso moltiplicare un intero con una tupla e viceversa, mi da una tupla che posso concatenare ad un altra tupla
# posso sempre moltiplicare un intero e un float, mi da un float che posso concatenare ad un int
# posso sempre moltiplicare tra di loro due interi ma NON posso concatenarli ad una tupla

# risposta corretta : E
    
    
    
# In[6]
# quale è il valore di len(t) alla fine del seguente frammento di codice ? 

a = 'python'
t = ('x', 'y', (1, 2, 3), 'z', a)
print(len(t))

# risposte : 
# A : 7
# B : 12
# C : 5
# D : 10
# E : 1

# risposta corretta : C

    

# In[7]
# sia n un intero positivo, cosa viene stampato dal seguente programma ? 

def f(a) :
    b = a/2
    if a > 0 : 
        b = a
    return b*b

b = n
x = f(b)
print(b)

# risposte : 
# A : (n-1)
# B : (n-1)**2
# C : n
# D : (n/2)**2
# E : (n//2)**2

# ATTENZIONE ALLA RICHIESTA DELL'ESERCIZIO 
# CHIEDE COSA VIENE STAMPATO, OVVERO print(b), b = n

# risposta corretta : C 

    

# In[8]
# siano a e b due stringhe in quale caso tra quelli proposti a < b ? 

# risposte : 
# A : se a è più corta di b
# B : se a inizia con 'f' e b inizia con 'q'
# C : se a è '90' e b è '100'
# D : se a ha meno spazi di b 
# E : mai

# a python non interessa la lunghezza della stringa ma piuttosto il carattere con cui inizia 
# se a = '90' e b = '100' ti da False perchè 9 < 1
# se a = 'f' e b = 'q' ti da True perchè q ha la precedenza su f 
# gli spazi non hanno importanza 

# risposta corretta : B



# In[9]
# per quale tipo di dato è consentito aggiungere ma non cancellare elemetenti ?

# risposte : 
# A : liste
# B : tuple
# C : stringhe
# D : nessuno dei tre

# le stringhe non posso modificarle, non posso ne aggiungere ne modificare
# le tuple e le liste le posso modificare aggiungendo elementi, 
# ma posso anche cancellare elementi attraverso il comando del()

# risposta corretta : D

    

# In[10]
# sia t una tupla di n elementi e si consideri la seguente operazione di assegnazione : 
# dove a sinistra dell'uguale compaiono k variabili. in quale caso questo tipo di operaizone è legale
    
# x0, x1, ... = t

# questa è l'operazione di unpacking e vale se e soltanto se t = k in termini numerici 
# oppure se le variabili a sinistra sono formate da un solo elemento, quindi se k = 1

# risposte : 
# A : solo se k è uguale a n 
# B : solo se k è uguale a 1
# C : se k è uguale a n oppure a 1
# D : se k è maggiore o uguale a n
# E : se k è minore o uguale a n

# risposta corretta : C






























