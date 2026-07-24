#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:23:39 2024

@author: valerio
"""

a=['zero', 'one']
d={}

for i in range(len(a)):
    d[a[i]]=i
print(a[d['one']+3+d[a[4]]])

# In[]

def enigma(x):
    if(x==''):
        return 1
    else:
        return 1+enigma(x[1:])
enigma('ciao')

# In[]

a='ciao'
n=len(a)
print(a[1:-1])
print(len(a[1:-1]))
print(a[:1])

# In[]
x=2
y='ciao'
if x > len(y):
    mx = x
else:
    mx = y
print(mx)

# In[]
n=2
ns = str(n)
ns = ns[::-1]
print(ns)

# In[]

x=int(input())
y=int(input())
c=(x*y)/2
d=(x*y//2)
print(c)
print(d)

# In[]

#La successione di Fibonacci è composta dagli interi 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...
#In particolare i primi due valori sono 0 e 1, ogni altro valore è dato dalla somma dei due precedenti.
#Scrivere un programma che chieda in input un numero n e stampi il valore in posizione n della successione è in posizione 0.

x0=0
x1=1
n=int(input("Inserisci la posizione del numero: "))
i=0
for i in range(2, n+1):
    x0, x1=x1, x0+x1
print(x1)

# In[]

def f(x, y=2):
    return x*y+x
print(f('ciao',7))

# In[]

def find_last(s, sub):
    """
    s e sub sono stringhe non vuote
    Restituisce l'indice dell'ultima occorrenza di sub in s,
    None se sub non è presente in s
    """
    # Trova l'indice dell'ultima occorrenza di 'sub' in 's' usando il metodo rfind
    index = s.rfind(sub)
    
    # Se l'indice è -1, significa che sub non è presente in s
    if index == -1:
        return None
    else:
        return index
print(find_last('ciao', 'iao'))

# In[]

a=[0,2,3,4]
b=a+[0]#cambia l'ordine dello zero in base a come sommo la lista con la lista con zero (in questo caso lo zero appare alla fine)
print(b)
c=b*2
print(c)

# In[]

def sas(stringa):
    stringa=stringa[0:3]+stringa[9:12]
    return stringa
    
stringa="ALJ-4543-BAU"
print(sas(stringa))

# In[]

def binario(bina):
    i=0
    c=''
    z=0
    numint=0
    while i<len(bina):
        if bina[i]!=' ':
            c+=bina[i]
        i+=1

    while z<len(c):
        numint+=int(c[z])*(2**(len(c)-z-1))
        print(c[z])
        print(numint)
        z+=1
    return numint
            
    
print(binario('10 10 11'))

# In[]

a='tuttofaredigitale.it'
print(a[::-1])#inverte tutti i caratteri
print(a[0:3])
print(a[:-3])#stampa da sx verso dx tranne gli ultimi 3 caratteri
print(a[-3:])#stampa da dx verso sx solo gli ultimi 3 caratteri
print(a[::2])#salta un carattere per arrivare fino alla fine
print(a[4::-1])#inverte i caratteri dalla pos 4

# In[]

def general_fun(l):
    i=0
    while i<len(l):
        j=1+i
        while j<len(l):
            if l[i]==l[j]:
                del l[j]
            else:
                j+=1
        i+=1
                
    print(l)
    
a=[1,2,2,4,7,8,7,9,1,5,5]
        
general_fun(a)


#modifica lista in input eliminando i duplicati

# In[]

def general_fun(l):
    
    new_list=[]
    for i in range (len(l)):
        for j in range (i+1,len(l)):
            if l[i]==l[j] and l[i] not in new_list:
                new_list.append(l[j]) 
    return new_list

a=[1,2,2,4,7,8,7,9,1,5,5]
        
print(general_fun(a))

#questo programma stampa i duplicati nella lista per poi inserirli in una nuova

# In[]

def general_fun(l):
    
    new_list=[]
    for i in range (len(l)):
        for j in range (i+1,len(l)):
            if l[i]==l[j] and l[i] not in new_list:
                new_list.append(l[j])   
            elif l[i]!=l[j] and l[i] not in new_list:
                new_list.append(l[i])
    return new_list

a=[1,2,2,4,7,8,7,9,1,5,5]
        
print(general_fun(a))

#questo programma stampa prima i duplicati e poi inserisci i valori che non lo sono controllando se già ci sono nella nuova lista

# In[]

a=input("Inserisci data di nascita in forma gg/mm/aaaa: ")
print("Sei nato nell'anno:", a[6:10])

# In[]

num_x = int(input('Quante volte devo stampare la X? '))
to_print = ''
to_print='x'*num_x
print(to_print)

# In[]

#Scrivere un programma che chieda all'utente due interi r e c e stampi un rettangolo di r righe e c colonne utilizzando il simbolo *.
#Ad esempio se c ed r fossero rispettivamente 9 e 4, l'output del programma dovrebbe essere

'''
*********
*********
*********
*********
'''

#Il programma non deve utilizzare gli operatori di concatenazione e ripetizione sulle stringhe.

r = int(input('Numero di righe '))
c = int(input('Numero di colonne '))

x = 0
while x < r:
    y = 0
    while y < c:
        print('*', end='')
        y += 1
    print('')
    x += 1
    
# In[]
#Modificare la soluzione dell'esercizio precedente in modo tale che venga mostrato soltanto il perimetro del rettangolo

r = int(input('Numero di righe '))
c = int(input('Numero di colonne '))

y = 0
while y < r:
    x = 0
    while x < c:
        if y == 0 or y == r-1 or x == 0 or x == c-1:
            print('*', end = '')
        else:
            print(' ', end = '')
        x += 1
    print('')
    y += 1

# In[]

#Scrivere un programma che chieda in input due stringhe a e b. Se b è sottostringa di a il programma stampi la posizione di a
#a partire dalla quale compare b. Altrimenti il programma stampi -1. Ad esempio se a fosse la stringa 'rinoceronte' e b la stringa 'noce', il programma
#stamperebbe 2
a = input('stringa 1: ')
b = input('stringa 2: ')
flag=False

if len(b)<len(a):
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j]==a[i] and flag==False:
                print(i)
                flag=True
else:
    print('-1')


# In[]

#Scrivere un programma che chieda all'utente due stringhe a e b, se queste hanno almeno una lettera in comune il programma stampi a in orizzontale e b
#in verticale in modo tale che si intersechino nella prima lettera che compare sia in a che in b

a = input('stringa 1: ')
b = input('stringa 2: ')
flag=False

for i in range(len(a)):
    for j in range(len(b)):
        if b[j]==a[i]:
            flag=True
        break

if flag==True:
    for x in range(len(b)):
        if x == j:
            print(a)
        else:
            print(' '*j+b[x])
            
# In[]

#Scrivere un programma che chieda in input due stringhe e le stampi allineate al centro. Ad esempio se le due stringhe fossero programmazione e Python,
#il programma stamperebbe

    #programmazione
        #Python

a = input('stringa 1: ')
b = input('stringa 2: ')

print(a)    

x=len(a)//2
print(" "*x+b)
    

# In[]

#Scrivere un programma che chieda in input una stringa, la stampi e ne evidenzi le vocali inserendo un carattere * al di sotto di queste.
#Ad esempio, se la stringa fosse programmazione il programma stamperebbe

#programmazione
#  *  *  * ** *

a = input('stringa: ')
print(a)
stringa=""

for i in range(len(a)):
    if a[i] in "aeiou":
        stringa+="*"
    else:
        stringa+=" "
print(stringa)


# In[]

#Scrivere un programma che chieda all'utente di inserire una sequenza di numeri e, per ogni numero inserito a partire dal terzo, stampi la media troncata
#ovvero la media dei valori inseriti scartando il valore minimo e massimo.

a = input('stringa di numeri: ')
media=0

for i in range(len(a)):
    media+=int(a[i])

media=(media-int(max(a))-int(min(a))-int(a[0])-int(a[1]))/(len(a)-2)
print(media)

# In[]

def find_last(s, sub):
    """
    s e sub sono stringhe non vuote
    Restituisce l'indice dell'ultima occorrenza di sub in s,
        None se sub non è presente in s
    """
    count=0
    
    if len(s)==0 and len(sub)==0:
        return True
    else:
        for i in range(len(s)):
            for j in range(len(sub)):
                if sub[j]==s[i]:
                    count=j
    return sub[count]
    
s="cio"
sub="ciao"

print(find_last(s, sub))

# In[]

#Si scriva una funzione che abbia tre parametri obbligatori (x, y e z) ed un parametro facoltativo (key) che sia una funzione che assegni a x, y e z un
#valore. La funzione restituisca il massimo tra x, y e z rispetto alla funzione key. Il valore predefinito per key sia la funzione identità.

def find_max(x,y,z,key=lambda l: l):
    return max(x,y,z,key=key)


x="ciao"
y="sososo"
z="x"

print(find_max(x, y, z, key=len))

# In[]

def f(L1, L2):
    
    """
    L1, L2 sono liste di numeri della stessa lunghezza
    Restituisce la somma degli elementi di L1 elevati
        alla potenza dell'elemento allo stesso indice
        in L2. Per esempio, f([1,2], [2,3]) restituisce 9
    """

    somma=0
    
    for i in range(len(L1)):
        somma+=(L1[i]**L2[i])
    return somma
        

L1=[1,2]
L2=[2,2]

print(f(L1, L2))

# In[]

#Scrivere una funzione denominata inverti_dizionario che prenda in input un dizionario d e restituisca un dizionario d_inv che abbia per chiavi i valori in
#d e d_inv[v] sia la lista di chiavi che d mappa in v.


def inv_dic(d):
   d_inv={}

   for k, v in d.items():
        d_inv[v]=k
   return d_inv  
    
d={'k0':2, 'k1':3, 'k2':4 }
print(inv_dic(d))

# In[]


#La somma armonica di un intero, n > 0, si può calcolare con la formula

    #1 + 1/2 + 1/3 + ... + 1/n

#Scrivete una funzione ricorsiva che la calcoli

def armonic(a):
    
    if a==0:
        return a
    
    else:
        return (1/a)+armonic(a-1)
    
a=5
print(armonic(a))


# In[]

def deep_count(t):
    
    '''
        Precondizione: t è una tupla che può contenere al suo interno
            tuple annidate
        Restituisce il numero di elementi numerici contenuti in t
            ed in tutte le tuple annidate
    '''
    
    c=0
    
    if type(t)==int or type(t)==float:
        return 1
        
    else:
        for x in t:
            c+=deep_count(x) #somma a c 1 se il tipo è un numero in modo ricorsivo
        return c
    
t=( 3.14, (2, 3), (2.71, (7, 5)), 9, (12, ( 4, )) )
print(deep_count(t))

# In[]

#Scrivere una funzione Python denominata deep_copy che cloni la lista in input e tutte le liste annidate che essa contiene

def deep_copy(L):
    copy=[]
    if type(L)==list:
        for x in L:
            copy.append(deep_copy(x))
        return copy
    else:
        return L
        
L=['oddio', [2,3], ['sas']]
print(deep_copy(L))


# In[]

"""
Scrivere una funzione denominata sort_by_type che prenda una lista che può contenere int, float o str. La funzione ritorni una nuova lista in cui gli int
precedano i float che precedano le str. Si risolva senza utilizzare il metodo sort.
"""

def sort_by_type(a):
    new_list=[]
    
    for x in a:
        if type(x)==int:
            new_list=[x]+new_list
        elif type(x)==float:
            new_list=[x]+new_list
        elif type(x)==str:
            new_list.append(x)

    return new_list

a=["rdyt",4.8,1]
print(sort_by_type(a))

# In[]

"""
Scrivere una funzione denominata inverti_dizionario che prenda in input un dizionario d e restituisca un dizionario d_inv che abbia per chiavi i valori
in d e d_inv[v] sia la lista di chiavi che d mappa in v. Esempio se

d = { 'k0': 'v0', 'k1': 'v1', 'k2': 'v0' }

allora

d_inv = { 'v0': ['k0', 'k2'], 'v1': ['k1'] }
"""

def inv_dict(d):
    d_inv={}
    for k,v in d.items():
        d_inv[v]=k
        
    return d_inv

d={'a':12, 'b':34, 'c':76}
print(inv_dict(d))

# In[]

"""
Si scriva una funzione Python, denominata sort_by_len, che riceva in input una lista di numeri (int o float) e la muti in modo che gli elementi siano ordinati
per numero di cifre crescenti.

Ad esempio se

a = [3.14, 3133, 8, 123456, 1.2345]

dopo l'esecuzione di sort_by_len( a ), a sarebbe

[8, 3.14, 3133, 1.2345, 123456]
"""

def sort_by_len(a):
    a=[str(x) for x in a]
    a.sort(key= lambda x: len(x))
    a=[float(x) for x in a]
    return a
    
    
    

a=[1,294.2,3,5,674,13]
print(sort_by_len(a))

# In[]

"""
Esercizio (dal Guttag)

La somma armonica di un intero, n > 0, si può calcolare con la formula

    1 + 1/2 + 1/3 + ... + 1/n

Scrivete una funzione ricorsiva che la calcoli.

"""

def sommarmonica(n):
    
    if n==1:
        return n
    else:
        return 1/n + (sommarmonica(n-1))
    
n=4
print(sommarmonica(n))

# In[]

def deep_count( t ):
    '''
    Precondizione: t è una che puà contenere al suo interno
        tuple annidate
    Restituisce il numero di elementi numerici contenuti in t
        ed in tutte le tuple annidate
    '''
    if type(t) in (float, int): # t è un numero
        return 1
    else:
        c = 0
        for x in t:
            c += deep_count(x)
        return c



