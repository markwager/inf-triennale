#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:32:29 2024

@author: valerio
"""

def cript(k, stringa):
    i=0
    b=''
    while i<len(stringa):
        b+=chr(ord(stringa[i])+k)
        i+=1
    return b

print(cript(3, 'ciao'))
    
# In[]
def decript(k, stringa):
    i=0
    b=''
    while i<len(stringa):
        b+=chr(ord(stringa[i])-k)
        i+=1
    return b

print(decript(3, 'fldr'))

# In[]

def coltz(n):
    c=n
    i=0
    a=''
    while c!=1:
        if c==1:
            return None
        elif c%2==0:
            c=c//2
        else: 
            c=c*3+1
        i+=1
        a+=str(c)+' '
    #return c
    return i

print(coltz(6))

# In[]

#Si scriva una funzione che riceve in input una sequenza di interi positivi e restituisca True se e solo se questi
#rappresentano una permutazione degli interi 1,2,...,n dove n è il numero di interi nella sequenza.

def perm(n):
    p=len(n)
    for i in range(1,p+1):
        if i not in n:
            return False
        else:
            return True
            
a=[3,2,1]
print(perm(a))

# In[]

#Scrivere una funzione che chieda in input un numero variabile di stringhe e le stampi allineate al centro.
#Ad esempio se le stringhe fossero programmazione, Python e funzione il programma stamperebbe

#programmazione
    #Python
   #funzione
   
def centering(*strings):
    max_len = 0
    for x in strings:
        max_len = max(max_len, len(x))
    for x in strings:
        num_spaces = (max_len - len(x))//2
        print(' '*num_spaces+x)
        
# In[]

#scrivere una funzione rimario, a cui vengono passati come parametri una lista di parole e una parola.
#si dovrà confrontare la parola inserita con quelle presenti nella lista, alla ricerca di rime intese come le ultime 3 lettere.

def rimario(stringhe,stringa):
    for i in stringhe:
        if i[-3:] == stringa[-3:]:
            return stringa[-3:]
        else:
            return False
        
print(rimario(['dormire', 'cacca'], 'presagire'))
#con join la lista non viene toccata, con append invece viene modificata        

# In[]

#scrivere una funione che, data una lista di numeri, resistuisce il secondo num più grande all'interno della lista

def secmajor(lista):
    massimo = lista[0]
    
    for n in lista:
        if n > massimo:
            massimo = n #cattura il valore max
    
    # Crea una nuova lista escludendo la prima occorrenza del massimo
    nuova_lista = []
    max_rim = False
    
    for i in lista:
        if i == massimo and max_rim==False:
            max_rim = True  # Salta la prima occorrenza del massimo
        else:
            nuova_lista.append(i) #la lista contiene tutti i numeri tranne 89, il valore max
    
    secmax=nuova_lista[0]
    
    for j in nuova_lista:
        if j > secmax:
            secmax=j
    return secmax
        
print(secmajor([1,9,89,4,12,6]))

# In[]

#lista di interi che genera poi nuova lista

def iter(L):
    b=[]
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]==L[j] and L[i] not in b:
                b.append(L[i])
    return b
            
print(iter([2,1,2,3,5,5]))


# In[]

def del_emptylist(lista):
    vuota = []
    n = 0
    while n < len(lista):
        if lista[n] == vuota:
            del lista[n]
        else:
            n += 1
    return lista

print(del_emptylist([[],[],4,'ciao']))

# In[]

def injection(l1,l2):
    for i in l1:
        for j in l2:
            if i in l2:
                return True
            else:
                return False
            
print(injection([1,2,3], [1,2,3]))

# In[]

def intersc(l1,l2): 
    i=0
    lista=l1+l2
    while i<len(lista):
        j=1+i
        while j<len(lista):
            if lista[i]==lista[j]:
                del lista[i]
            else:
                j+=1         
        i+=1

    return lista

print(intersc([1,2,3], [5,3,1]))

# In[]

def Min(a, key=None): #key=None, valore di default, quindi se key==None massimizza e.
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
        
    r_min=key(a[0]) #restituisce un valore fissato arbitrariamente da noi (può essere 0,1...); in questo caso -2
    for e in a:
        if key(e)<r_min:
            r_min=key(e)
    return r_min

def t1(e):
    return e[1]

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]
print(Min(a, key=t1)) #ritorna il valore massimo confrontando tutti i valori interi grazie a key (confronta gli elementi al secondo indice)
print(Min(a))


# In[]


#scrivere una funzione che elimina i duplicati (modifica la lista in input),
#crea una tupla a partire dalla lista modificata e restituisce l'elemento massimo e minimo

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
        
   #il secondo while shifta dal secondo elemento in poi nella lista e confronta il primo col secondo, il secondo col terzo ecc...
   #successivamente incrementa il valore di j se i due valori sono diversi. Alla fine del secondo ciclo, il valore i incrementa
   #e e il valore j viene fissato poi a 2 (invece all'inizio era 1`)
                
    print(l)
    
    r_min=l[0]
    r_max=l[1]

    for e in l:
        if e<r_min:
            r_min=e
        elif e>r_max:
            r_max=e
    print(r_min)
    print(r_max)


a=[1,2,2,4,7,8,7,9,1,5,5]
    
general_fun(a)



# In[]
def sono_anagrammi(stringa1, stringa2):
    trovato=False
    
    # Se le lunghezze sono diverse, non possono essere anagrammi
    if len(stringa1) != len(stringa2):
        return False
    
    elif len(stringa1) == len(stringa2):
        # Iteriamo su ogni carattere in stringa1
        
        stringa2_lista = list(stringa2)
        for char in stringa1:
            trovato = False
            # Creiamo una lista temporanea per contenere i caratteri rimanenti
            nuova_lista = []
            
            for i in range(len(stringa2_lista)):
                if stringa2_lista[i] == char and trovato==False:
                    trovato = True  # Il carattere è stato trovato, non aggiungerlo alla nuova lista
                else:
                    nuova_lista.append(stringa2_lista[i])  # Aggiungi il carattere alla nuova lista se è diverso
    
            # Dopo aver iterato, aggiorniamo stringa2_lista
            stringa2_lista = nuova_lista
            
            #il primo for shifta i char in stringa1 e svuota nuova_lista
            #il secondo for shifta i char in stringa2_lista e controlla se sono uguali:
            #se sì trovato=True (non fare nulla praticamente) altrimenti lo metti nella nuova_lista e la eguagli alla stringa2_lista
            #infine reitera tutto però svuotando la nuova_lista e cos' la stringa2_lista è comunque uguale all'ultima volta
            #facendo così man mano la stringa2_lista si svuota se non ci sono più caratteri uguali
            
        # Se non abbiamo trovato il carattere, non sono anagrammi
        if len(stringa2_lista)>0:
            return False
        
        # Se tutti i caratteri sono stati trovati e rimossi, sono anagrammi
        elif len(stringa2_lista) == 0:
            return True

print(sono_anagrammi('ciao', 'caio'))
    

# In[]

#scrivere una funzione che, data in input una lista che può contenere liste, modifichi la lista in input eliminando le liste
#facendo sì che si abbia un'unica lista

def appiat(L):
    i=0
    j=0
    while i<len(L):
        if type(L[i])==type(L):
            L+=(L[i][0:])
        i+=1
    print(L)
    
    while j<len(L):
        if type(L[j])==type(L):
            del L[j]
        else:
            j += 1  # Incrementa solo se non è una lista
    return L

L=[1,[2],3,[1,2,3,4],[8]]
print(appiat(L))

# In[versione + efficiente e più funzionante]

def appiat(L):
    i=0
    while i<len(L):
        if type(L[i])==type(L):
            L[i:i + 1] = L[i] #sostituisce la lista interna con i suoi elementi interni
        i+=1
    return L

L=[1,[2],3,[1,2,3,4],[8]]
print(appiat(L))

#questo codice ti da l'ordine originale in confronto al precedente

# In[]

def deep_sum(a):
    
    b = 0
    for e in a:
        if type(e) != list:
            b+=e
        else:
            b+=(deep_sum(e))
    return b

a = [ 1, [0, 3.14, 0], 100, [2, 5] ]
b = deep_sum(a)
print(b)

# In[]

def deep_inv(a):
    
    b = 0
    for e in a:
        if len(a) == 1:
            return a
        else:
            b=(deep_inv(a[1:])) #meno il primo char
            b+=a[0]
    return b

a = 'ciao'
b = deep_inv(a)
print(b)

#complessità temporale n-1+n-2+..+1=n(n-1)/2=O(n^2)

# In[efficienza senza usare lo slicing]

def deep_inv(a, i=0):
    
    if i==len(a)-1:
        return a[i]
    else:
        b=(deep_inv(a,i+1)) #meno il primo char
        b+=a[i]
    return b

a = 'ciao'
b = deep_inv(a)
print(b)

#complessità temporale O(n)
#complessità spaziale O(n^2) per via del contenuto dentro i frame chiamati (vedi su python tutor)

# In[ancora più efficiente]


def deep_inv(a, i=0):
    if type(a)==str:
        a=list(a)
    if i==len(a)-1:
        return a[i]
    else:
        b=(deep_inv(a,i+1)) #meno il primo char
        b+=a[i]
    return b

a = 'ciao'
b = deep_inv(a)
print(b)

#complessità temporale O(n)
#complessità spaziale O(n)

# In[]

#scrivere una funzione che abbia in input una lista con numeri ordinati in ordine crescente non negativi, ritorna il + piccolo
#mancante, altrimenti restituisce -1. Non ci devono essere ripetizioni

def ricerca_num(a):

    lx, rx = 0, len(a)-1
    
    while lx <= rx:
        cx = int((lx+rx)/2)
        if cx<a[cx]:
            rx=cx-1
        elif cx==a[cx]:
            lx=cx+1
    return lx
            
a=[0,1,2,3,4,5,10,44,51]

print(ricerca_num(a))

#la funzione sposta verso sinistra rx se cx è minore da a[cx]. Se cx è uguale a a[cx] allora sposta lx verso destra.
#esiste la condizione cx<a[cx] perchè comunque cx non può essere maggiore di a[cx]: non ci possono essere ripetizioni e poi
#i numeri sono messi in ordine crescente. Alla fine ritorna il valore per cui si ferma il loop, cioè lx

# In[]

def deep_sum(a):

    for e in a:
        if e=='osvaldo':
            return True
        elif type(e)==list:
            if deep_sum(e):
                return True
    return False

a = [ 1, [0, 3.14, 'osvaldo'], 100, [2, 5] ]
b = deep_sum(a)
print(b)

# In[]

#ho una sequenza di numeri ordinati in una lista, trovare la posizione dell'occorrenza più a sx di k di a

def ricerca_intervallo(a, k):
    lx, rx = 0, len(a) - 1
    result = 0

    while lx <= rx:
        cx = (lx + rx) // 2
        if a[cx] == k:
            result = cx  
            rx = cx - 1  # Continua la ricerca a sinistra per trovare la prima occorrenza
        elif a[cx] < k:
            lx = cx + 1 
        else:
            rx = cx - 1
            
        '''
        Le ultime due condizioni servono per cercare
        a sx invece che a dx (come nel programma del prof che si cerca a dx)
        
        '''
    return result

    if k!=a[cx]:
        return -1
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=9

print(ricerca_intervallo(a,k))

# In[]


def ricerca_intervallo(a, k):
    lx, rx = 0, len(a) - 1
    result = 0

    while lx <= rx:
        cx = (lx + rx) // 2
        if a[cx] == k:
            result = cx  
            lx = cx + 1  # Continua la ricerca a dx per trovare la prima occorrenza
        elif a[cx] < k:
            rx = cx - 1 
        else:
            lx = cx + 1
            
        '''
        Le ultime due condizioni servono per cercare
        a dx invece che a sx
        '''
    return result

    if k!=a[cx]:
        return -1
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=9

print(ricerca_intervallo(a,k))

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
        if k == a[cx] and (cx==len(a)-1 or a[cx+1]>k):
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

# In[]

def binary_search_left(a, k):
    n = len(a)
    lx, rx = 0, len(a)-1

    while lx <= rx:
        cx = int( (lx+rx)/2 )
        if k > a[cx]:
            lx = cx + 1
        elif k == a[cx] and (cx == 0 or a[cx-1] < k):
            return cx
        else:
            rx = cx-1

    return -1

"""
Sia n la lunghezza della lista.
Complessità temporale: O(log n)
Complessità spaziale: O(1)
"""

lista = [1,3,4,4,4,4,5,7,7,7,7,10,10,12,12,15,17]
k = 4
print("Input: ", lista, k)
print("Output: ", binary_search_left(lista, k))

# In[]

#scrivere una funzione in cui si ha in input una lista di numeri ordinati in modo crescente. Si cerca la
#prima e l'ultima occorrenza del numero cercato

def ricerca_intervallo(a, k):
    lx1, rx1 = 0, len(a)-1
    lx2, rx2 = 0, len(a)-1
    pos1=0
    pos2=0

    while lx1 <= rx1:
        cx = (lx1 + rx1) // 2
        if a[cx] == k:
            pos1 = cx  
            lx1 = cx + 1  # Continua la ricerca a dx per trovare la prima occorrenza
        elif a[cx] < k:
            rx1 = cx - 1 
        else:
            lx1 = cx + 1

    while lx2 <= rx2:
        cx = (lx2 + rx2) // 2
        if a[cx] == k:
            pos2= cx  
            rx2 = cx - 1  # Continua la ricerca a sinistra per trovare la prima occorrenza
        elif a[cx] < k:
            lx2 = cx + 1 
        else:
            rx2 = cx - 1
            
        '''
        Le ultime due condizioni servono per cercare
        a sx invece che a dx (come nel programma del prof che si cerca a dx)
        
        '''
    return pos1,pos2

    if k!=a[cx]:
        return -1
    
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=5

print(ricerca_intervallo(a,k))

# In[]

#scrivere una funzione in cui si ha in input una lista di numeri ordinati in modo crescente. Si cerca la
#prima e l'ultima occorrenza del numero cercato

def ricerca_intervallo(a, k):
    lx1, rx1 = 0, len(a)-1
    lx2, rx2 = 0, len(a)-1
    pos1=0
    pos2=0
    
    while lx1 <= rx1:
        cx = int( (lx1+rx1)/2 )
        if k == a[cx] and (cx==len(a)-1 or a[cx+1]>k):
            pos1=cx
            break
        elif k < a[cx]:
            rx1 = cx-1
        else:
            lx1 = cx+1
            

    while lx2 <= rx2:
        cx = int( (lx2+rx2)/2 )
        if k > a[cx]:
            lx2 = cx + 1
        elif k == a[cx] and (cx == 0 or a[cx-1] < k):
            pos2=cx
            break
        else:
            rx2 = cx-1
    
    return pos2,pos1

    if k!=a[cx]:
        return -1
    
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=9

print(ricerca_intervallo(a,k))


# In[]

#scrivere una funzione in python che, data una lista binaria a, ordina la lista a. La funzione deve avere un costo temporale lineare in len(a)
#e un costo spaziale costante

def sort_bin(a):
    num_z=0
    for e in a:
        if e==0:
            num_z+=1
    
    k=0
    
    while num_z:
        a[k]=0
        num_z-=1
        k+=1
    
    for k in range(k, len(a)):
        a[k]=1
        
    return a
        
a=[0,0,0,0,1,1,1,0,0,0]

print(sort_bin(a))

#praticamente questa funzione conta il numero di 1 presenti nella lista, mette a 0 tutte le k posizioni nella lista a e mette a 1 le restanti
#posizioni da k alla lunghezza della lista

# In[]

#scrivere una funzione in python che implementi l'algoritmo della ricerca binaria usando la ricorsione

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

# In[]
#si hanno due liste ordinate di interi, restituisce una nuova lista che p l'intersezione delle due liste

def merge_intersec(a,b):
    
    i, j=0, 0
    c=[]
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            c.append(a[i])
            i+=1
            j+=1
        elif a[i]<b[j]:
            i+=1
        else:
            j+=1
            
    return c
    
a=[0, 1, 2, 4, 5, 6, 14]
b=[0, 2, 4, 5, 6, 9]
    
print(merge_intersec(a, b))

# In[]
#funziona lambda che ritorna True se la parola è palindroma, altrimenti False

x=lambda x: True if x==x[::-1] else False
print(x('girafarig'))

# In[]

#funzione lambda che ritorna lista di tuple ordinate per il secondo elemento di ciascuna tupla

a=[('A',6), ('B',-2), ('C', 0), ('D', 5), ('E', 3)]

L=sorted(a, key=lambda a:a[1])

print(L)


# In[]

#scrivere una fuznione tale che, date due liste in input ordinate, restituisca una lista che è la differenza tra le due liste. Ovvero la nuova
#lista: ovvero la nuova lista deve contenere tutti gli elementi della prima lista tranne quelli in comune nella seconda.
#La funzione deve avere una complessità temporale: len(l1)+len(l2), quella spaziale deve essere costante

def merge_difference(a,b):
    
    i, j=0, 0
    c=[]
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            i+=1
            j+=1
        elif a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(a[i])
            j+=1
            
    return c
    
a=[0, 1, 2, 4, 5, 6, 14]
b=[0, 2, 4, 5, 6, 9]
    
print(merge_difference(a, b))

# In[]

#scrivere una fuznione tale che, date due liste in input ordinate, effettui l'operazione merge in loco (senza una struttura dati d'appoggio)
#in particolare se len(l1)=n e len(l2)=m, allora la funzione deve scrivere in l1 i primi elementi più piccoli e in l2 gli elementi rimanenti.

def merge_loco(a,b):
    n=len(a)
    m=len(b)
    i,j=0,0
    
    while i<n and j<m:
        if a[i]==b[j]:
            i+=1
            j+=1
        elif a[i]<b[j]:
            i+=1
        else:
            a[i],b[j]=b[j], a[i]
            i+=1
            b.sort()
            
    return a,b
        
a=[0, 1, 2, 4, 5, 6, 14]
b=[3, 7, 8, 8.5, 9, 12, 13]

print(merge_loco(a, b))

#la funzione in questione scambia i posti se a[i]>b[j] e poi ordina la lista b

# In[]

#risolvere la torre di Hanoi con una funione (ricorsiva)

def torre_di_hanoi(n, origine, destinazione, mezzo):
    if n == 1:  # Caso base: un solo disco
        print("Sposta il disco 1 da " + origine + " a " + destinazione)
        return
    # Passo ricorsivo: sposta n-1 dischi dall'origine all'ausiliario
    torre_di_hanoi(n - 1, origine, mezzo, destinazione)
    # Sposta il disco più grande rimanente dall'origine alla destinazione
    print("Sposta il disco " + str(n) + " da " + origine + " a " + destinazione)
    # Sposta i n-1 dischi dall'ausiliario alla destinazione
    torre_di_hanoi(n - 1, mezzo, destinazione, origine)
    
torre_di_hanoi(3, "A", "C", "B")

# In[]

#funzione che ritorna true se due stringhe sono anagrammi

def anagramma(a,b):
   
   if len(a)!=len(b):
       return False
   
   x=sorted(a)
   y=sorted(b)
   
   if x==y:
       return True
   else:
       return False
   
   print(x,y)
    
    
#ha complessità temporale O(nlogn) sempre per via del sorted
#peer ottimizzare l'algoritmo si possono usare i dizionari in modo tale da aver un costo medio di O(n)
   

print(anagramma('maroo','romao'))

#si possono ordinare a e b

# In[]


def anagramma(a,b):
    da, db={}, {}
    
    for x in a:
        da[x]=da.get(x,0)+1 #O(1) in media
    
    for x in a:
        db[x]=db.get(x,0)+1
        
    for x in da:
        if da[x]!=db.get(x,0): #O(1) in media
            return False
    
    for x in db:
        if da.get(x,0)!=db[x]:
            return False
    return True
    
print(anagramma('maroo','romao'))
        

# In[]
#calcolare la complessità temporale di del() nel caso medio applicata ad un elemeto di una lista.
#nel risolvere l'esercizio si tenga conto che la cancellazione di un elemento in pos i della lista a richiede i*c operaz. per una costante c
#la funzione del() ha nel caso peggiore un costo lineare perchè va a cercare l'elemento da eliminare
#nel caso medio si deve assumere una probabilità equivalente su tutta la lista per trovare l'elemento x. Perciò si avrà una somma che parte da 0
#fino a n-1 dove n è il numero di elementi 

a=[1,2,3,4]

del(a[0])

print(a)

# In[]

#scrivere una funzione che, date due liste l1 e l2, ritorna la differenza tra l1 e l2 con costo medio len(a)+len(b)

def merge_difference_diz(a,b):
    
    i, j=0, 0
    dc={}
    c=[]
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            i+=1
            j+=1
        elif a[i]<b[j]:
            dc[i]=a[i]
            i+=1
        else:
            dc[i]=a[i]
            j+=1
        
    c=dc.values()
    return c      
    
a=[0, 1, 2, 4, 5, 6, 14]
b=[0, 2, 4, 5, 6, 9]
    
print(merge_difference_diz(a, b))

# In[]

#scrivere una funzione che dato un dizionario con coppie del tipo (key, list[int]), crea un dizionario con coppie del tipo (sum(list[int]),key).

def sum_inv_diz(d):
    dc = {}  # Inizializza il dizionario di output
    for k, v in d.items():
        # Calcola la somma della lista di valori
        total = sum(v)
        # Assegna al nuovo dizionario
        dc[total] = k
    return dc
            
d={'a':[7,3], 'b':[1,4], 'c':[10,1]}
print(sum_inv_diz(d))


# In[]

#scrivere una funzione che data una lista words di parole e una stringa letters di caratteri, stampa in output tutte e sole le parole in words che possono
#essere ottenute usando un sottoinsieme delle lettere in letters

def words_letters(w,l):
    common=[]
    com=[]
    for i in w:
        for j in l:
            if j in i and j not in common:
                common.append(j)
    print(common)
            
w=["cane", "gatto", "tartaruga", "canto"]
l="anetougc"

print(words_letters(w, l))

# In[]

def words_letters(w, l):
    common = []
    cum=[]
    
    i = 0
    while i < len(w):
        c = 0
        while c < len(w[i]):
            j = 0
            while j < len(l):  
                if l[j] == w[i][c] and w[i] not in common:  # Confronta i caratteri
                      # Aggiungi solo se non già presente
                    common.append(l[j])
                      # Esci dal ciclo su l per passare al prossimo carattere di w[i]
                j += 1
            c += 1  # Passa al carattere successivo della parola corrente
        i += 1  # Passa alla parola successiva
    
        
# Esempio di utilizzo
w = ["cane", "gatto", "tartaruga", "canto"]
l = "anetougc"

print(words_letters(w, l))