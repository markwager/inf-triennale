#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:02:58 2025

@author: valerio
"""

"""
Scrivere una funzione rimario, a cui vengono passati come parametri una lista di parole e una parola inserita dall'utente tramite
funzione input.

La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle presenti nell'elenco, alla ricerca di rime, intese
come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.
"""

def rimario(lista_parole, parola):
    a=" "
    rime=[]
    for x in lista_parole:
        if parola[-3:]==x[-3:]:
            rime.append(x)
            a=", ".join(rime)
    print(a)

lista_parole=["cagare","pisciare","stocazzo"]
parola="mangiare"

rimario(lista_parole,parola)
# In[]

"""
Scrivere una funzione in Python che, data una lista di numeri, restituisce il secondo numero più grande all'interno della lista.
"""

def secondbigger(L):
    massimo=L[0]
    mass=L[0]
    indice=0
    for x in range(len(L)):
        if L[x]>massimo:
            massimo=L[x]
            indice=x
            
    del L[indice]
    
    for y in range(len(L)):
        if L[y]>mass:
            mass=L[y]
            
    return mass
            
    
L=[12,89,24,66,1]
print(secondbigger(L))

# In[]

"""
Scrivere una funzione in Python che, date una lista di interi, genera un'altra lista contenente solamente gli elementi duplicati.
"""

def listdupl(L):
    lista=[]
    for x in range(len(L)):
        for y in range(x+1,len(L)):
            if L[x]==L[y] and L[x] not in lista:
                lista.append(L[x])
    return lista

L=[1,2,4,4,7,5,4,8,9,0,9]
print(listdupl(L))

# In[]

"""
Scrivere una funzione in python che, data una lista, rimuove da quest'ultima tutte le liste vuote contenute all'interno.
"""

def removempty(L):
    tmp=[]
    for x in range(len(L)):
        if L[x]!=[]:
            tmp.append(L[x])
    i = 0
    while i < len(tmp):
        L[i] = tmp[i]
        i += 1
        
    # i è la posizione del primo elemento da eliminare da a e ho la lista
    #L=[1,2,4,4,4,8,9,9,9] con i=8
    while i < len(L):
        del(L[-1])
    #cancella i rimanenti elementi che non ci servono
    return L

L=[1,2,4,4,[],4,8,9,9,[],[]]
print(removempty(L))

# In[]

"""
Scrivere una funzione in Python che, date due liste l1 e l2, restituisce True se ogni elemento di l1 è contenuto anche in l2,
False altrimenti.
"""
def is_in(l1,l2):
    for x in l1:
        if x not in l2:
            return False
    return True

l1=[1,4,5,2,2,1]
l2=[1,4,5,2,2,1]
print(is_in(l1,l2))

# In[]

"""
Scrivere una funzione in Python che, date due liste l1 e l2, restituisce una lista senza duplicati che è l'intersezione delle due
liste l1 e l2.
"""

def intersec(l1,l2):
    lista=[]
    for x in range(len(l1)):
        for y in range(len(l2)):
            if l1[x]==l2[y] and l1[x] not in lista:
                lista.append(l1[x])
    return lista
    

l1=[1,3,4,5]
l2=[1,3,4,2,9,76,5]

print(intersec(l1, l2))

# In[]

"""
Scrivere una funzione Min in python che, data in input una lista a e una funzione key, restituisce l'elemento e in a tale che key(e)
= min(key(x) per x in a); se key è None, restitusce il minimo nella lista.
"""


def Min(a, key=None):
    
    
    def identity(e): #ritorna la tupla
        return e
    
    if key == None:
        key = identity #se la chiave non è specificata dall'utente questa viene eguagliata alla funzione identità
        
    v_min = key(a[0]) #tupla stessa in caso di key==None, secondo elemento in caso di key==t1
    r_min = a[0]

    for e in a:
        if key(e) <v_min:#in caso di t1: se il secondo elemento nella tupla è minore del secondo nella prima tupla fissa, aggiorna il minimo fisso
            v_min, r_min = key(e), e
            
    return r_min
    #r_min mi restituisce la tupla, v_min il valore nella tupla

def t1(e):
    return e[1] #restituisce il secondo elemento della tupla
    
a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

print(Min(a))
print(Min(a, key=t1))

# In[]

def Min(L, key=None):
    
    if key==None:
        minimo=L[0]
        for x in L:
            if x<minimo:
                minimo=x
        return minimo
    
    else:
        minimo=key(L[0])
        for x in L:
            if key(x)<minimo:
                minimo=key(x)
        return minimo

L=[("a",1), ("b",2), ("c",3), ("d",4), ("e",5)]
print(Min(L,key= lambda x: x[0]))

# In[]

def Max(a, key=None):
    '''
    Input: a una lista, key una func
    Output: e in a tale che key(e) = max(key(x) per x in a)
        se key è None massimizza e
    '''
    
    def identity(e):
        return e
    
    
    if key == None:
        key = identity
        
    v_max = key( a[0] )
    r_max = a[0]

    for e in a:
        if key(e) > v_max:
            v_max, r_max = key(e), e
            
    return r_max


def t1(e):
    return e[1]
    
a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

print(Max(a))
print(Max(a, key=t1))

# In[]

"""
Scrivere una funzione in python che, data una lista di interi in input, esegue le seguenti operazioni:

    rimuove i duplicati dalla lista in input (modificare la lista in input);
    crea una tupla a partire dalla lista modificata;
    restituisce l'elemento massimo e l'elemento minimo nella tupla;

"""

def oplist(L):
    
    tmp=[]
    
    for x in range(len(L)):
        for y in range(x+1, len(L)):
            if L[x]!=L[y] and L[x] not in tmp:
                tmp.append(L[x])
    
    i = 0
    while i < len(tmp):
        L[i] = tmp[i]
        i += 1
        
    # i è la posizione del primo elemento da eliminare da a
    while i < len(L):
        del(L[-1]) #costo costante
        
    Tupla=tuple(L)
    
    massimo=Tupla[0]
    minimo=Tupla[0]
    
    j=0
    
    while j<len(Tupla):
        if Tupla[j]>massimo:
            massimo=Tupla[j]
        if Tupla[j]<Tupla[j]:
            minimo=Tupla[j]
        j+=1
    
    print(massimo)
    print(minimo)
    print(L)
    print(Tupla)
    

L=[1,3,5,6,7,3,1,90,23,66,88,66]
oplist(L)

# In[migliore]

def remdupl(L):
    
    d={}
    
    for x in L:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    
    tmp=[k for k,v in d.items() if v==1]
    
    i=0
    while i<len(tmp):
        L[i]=tmp[i]
        i+=1
        
    while i<len(L):
        del(L[-1])
    
    print(L)
    
    tupla=tuple(L)
    
    print(max(tupla))
    print(min(tupla))

L = [1,2,3,44,56,1,33,55,56]
remdupl(L)



# In[]

"""
Scrivere una funzione in python che, date due stringhe in input, restituisce True se le due stringhe sono tra loro anagrammi, False
altrimenti.

Vi ricordo che, date due parole p1 e p2, la parola p1 è un anagramma della parola p2 se spostando i caratteri di p1 è possibile
ottenere la parola p2 e viceversa.
"""

def bubble_sort(a, key=None):
    def identity(e):
        return e

    n = len(a)

    if key == None:
        key = identity

    for c in range(n - 1):
        # se non effettua scambi, la lista è ordinata
        terminato = True
        for i in range(n - 1 - c):
            if key(a[i]) > key(a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                terminato = False
        if terminato:
            # la lista è ordinata
            break

def anagramma(stringa1,stringa2):
    
    str1=list(stringa1)
    str2=list(stringa2)
    
    bubble_sort(str1)
    bubble_sort(str2)
    #si ordinano entrambe le stringhe secondo l'ordine lessico-grafico
    #così se ci sono duplicati comunque si nota con l'if dopo
    
    if str1 != str2:
            return False
    return True
    
stringa1="riso"
stringa2="orsi"
print(anagramma(stringa1,stringa2))

# In[]

"""
Scrivere una funzione che, data in input una lista che può contenere liste, modifichi la lista in input appiattendola, cioè la lista
deve contenere tutti gli elementi originali ma eliminando le liste annidate. Guardate l'esempio per capire cosa si intende.
"""
def appiat(L):
    
    tmp=[]
    
    for x in L:
        if type(x)==list:
            for y in x:
                tmp.append(y)
        else:
            tmp.append(x)
    
    i=0
    while i<len(tmp):
        if i<len(L):
            L[i]=tmp[i]
        else:
            L.append(tmp[i])
        
        i+=1
        
    while i<len(L):
        del(L[-1])
    return L
    

L=[[1,2],3,[4,5,6],[7,8,9]]
print(appiat(L))

# In[appiat ricosriv]

def appiat(L):
    result = []
    for item in L:
        if type(item)==list:
            for subitem in appiat(item):
                result.append(subitem)
        else:
            result.append(item)
    return result

# Esempio di test
L = [[1, 2], 3, [4, [5, 6]], [7, 8, [9, [10]]]]
print(appiat(L))

# In[]

"""
Scrivere una funzione in Python che, data una lista composta da interi e sottoliste annidate (composte da interi e altre sottoliste),
restituisce in output la somma di tutti gli interi.
"""

def sommaint(L):
    
    sum = 0
    for e in L:
        if type(e) is not list:
            sum += e
        else:
            sum += sommaint(e)
    return sum

L=[1,2,5,[20,3,1,[40,6,3],2,5,6],5,[7,8]]
print(sommaint(L))

# In[]

"""
Scrivere una funzione in python che, data una stringa in input, ritorna in output la stringa invertita. Fare questo usando la
ricorsione e usando unicamente l'operazione di concatenazione tra stringhe.
"""

def invertita(s):
    if len(s) == 1:
        return s[0]
    else:
        reversed = invertita(s[1:])
        reversed += s[0]
        return reversed 

s="ciao"
print(invertita(s))

#costo quadratico per via di slicing

# In[]

def reversed_recursive_much_better(s, i = 0):
    if type(s) is str:
        l = []
        for c in s:
            l.append(c)
        s = l
    if i == len(s)-1:
        return s[i]
    else:
        reversed = reversed_recursive_much_better(s, i+1)
        reversed += s[i]
        return reversed
"""
Sia n la lunghezza della stringa, dunque n è anche la lunghezza della
lista d'appoggio creata.
Complessità temporale: O(n), in quanto vengono fatte n chiamate ricorsive
e in ogni chiamata ricorsiva si effettuano un numero costante di operazioni.
Complessità spaziale: O(n+n)=O(n) dato che vengono aperti n frame dalle
chiamate ricorsive e viene mantenuta una lista ausiliaria contenente tutti i
caratteri della stringa.
"""

print(reversed_recursive_much_better("programmazione")) 

# In[]

"""
Scrivere una funzione in Python che, data una lista di numeri interi distinti non negativi ordinati in modo crescente,
restutisce il più piccolo elemento non negativo mancante in essa. Se non ci sono elementi mancanti, restituisce -1.
"""

def mancante(L):
    i=0
    
    while i <len(L):
        if i!=L[i]:
            return i
        i+=1

L=[0,1,2,3,4,5,7,9,11]
print(mancante(L))

# In[]

def mancante(L):
    num = 0
    i = 0
    while i < len(L):
        if num != L[i]:
            print(num)
            num += 1  # Try next number without moving to next L[i]
        else:
            num += 1
            i += 1

L = [0, 1, 2, 3, 4, 6, 9, 10]
mancante(L)


# In[]

#oppure

def find_smallest_missing(nums):
    n = len(nums)
    lx, rx = 0, n-1

    while lx <= rx:
        cx = int((lx+rx)/2)
        if cx == nums[cx]:
            lx = cx+1
        else:
            rx = cx - 1

    return lx
"""
Sia n la lunghezza della lista.
Complessità temporale: O(log n)
Complessità spaziale: O(1)
"""

print(find_smallest_missing([1,2,6,7,10,11,13]))

# In[]

def search_osvaldo(L):
    for x in L:
        if x=="osvaldo":
            return True
        elif type(x) == list:
           if search_osvaldo(x):  # Ricorsione per sottoliste
               return True
    return False  # Non trovato

L=[1,2,3,[1,2,3,4],[1,5,4,2,[1,2,"osvaldo"],4,3,2]]
print(search_osvaldo(L))

# In[]

"""
Scrivere una funzione in Python che, data una lista a di numeri ordinati in modo non decrescente ed un numero k, restituisce
la posizione dell'occorrenza più a sinistra di k in a . Se k non è in a , ritorna -1.
"""

def ricerca_intervallosx(a, k):
   lx, rx = 0, len(a) - 1
   result = -1  # Valore predefinito se k non è trovato

   while lx <= rx:
        cx = (lx + rx) // 2
        if a[cx] == k:
            result = cx  # Salva la posizione trovata
            rx = cx - 1  # Continua la ricerca a sinistra
        elif a[cx] > k:
            rx = cx - 1  # Restringi intervallo a sinistra
        else:
            lx = cx + 1  # Restringi intervallo a destra
            
   return result
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=7

print(ricerca_intervallosx(a,k))

# In[]

def ricerca_intervallodx(a, k):
    lx, rx = 0, len(a) - 1
    result = -1  # Valore predefinito se k non è trovato

    while lx <= rx:
        cx = (lx + rx) // 2
        if a[cx] == k:
            result = cx  # Salva la posizione trovata
            lx = cx + 1  # Continua la ricerca a destra
        elif a[cx] > k:
            rx = cx - 1  # Restringi intervallo a sinistra
        else:
            lx = cx + 1  # Restringi intervallo a destra
            
    return result

   
a=[1,5,5,7,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=7

print(ricerca_intervallodx(a,k))

# In[]

"""
Scrivere una funzione in Python che, data una lista a di numeri ordinati in modo non decrescente ed un numero k , restituisce la
posizione della prima occorrenza di k in a e la posizione dell'ultima occorrenza di k in a . Se k non è in a , ritorna -1.
"""

def ricerca_intervallo(a, k):
    lx, rx = 0, len(a) - 1
    prima_occorrenza, ultima_occorrenza = -1, -1

    # Cerca la prima occorrenza
    while lx <= rx:
        cx = (lx + rx) // 2
        if a[cx] == k:
            prima_occorrenza = cx
            rx = cx - 1  # Continua a cercare a sinistra
        elif a[cx] > k:
            rx = cx - 1
        else:
            lx = cx + 1

    # Se la prima occorrenza non è stata trovata, k non è presente
    if prima_occorrenza == -1:
        return -1

    # Resetta i limiti per cercare l'ultima occorrenza
    lx, rx = 0, len(a) - 1

    # Cerca l'ultima occorrenza
    while lx <= rx:
        cx = (lx + rx) // 2
        if a[cx] == k:
            ultima_occorrenza = cx
            lx = cx + 1  # Continua a cercare a destra
        elif a[cx] > k:
            rx = cx - 1
        else:
            lx = cx + 1

    return prima_occorrenza, ultima_occorrenza
    
   
a=[1,5,5,7,7,7,9,9,10,13,13,14,17,19,19,19]
k=9

print(ricerca_intervallo(a,k))

# In[]

"""
Scrivere una funzione in Python che, data una lista binaria a, cioè contenente unicamente elementi in {0,1},
ordina la lista a. La funzione deve avere complessità temporale lineare in len(a) e complessità spaziale costante.
"""

def binord(L):
    
    count=0
    
    for x in range(len(L)):
        if L[x]==1:
            count+=1
    
    y=0
    
    while y < len(L):
        if L[y]==1:
            del L[y]
        else:
            y+=1
    
    for x in range(count):
        L.append(1)
    
    return L

#costo O(n**2)
    

L=[1,0,0,1,1,0,1,1,1,0,0,0]
print(binord(L))

# In[]

def binord(L):
    
    count=0
    
    for x in range(len(L)):
        if L[x]==1:
            count+=1
    
    for i in range(len(L) - count): #da 0 fino al numero di 1 che ho trovato metto 0
        L[i] = 0
    # Assegna gli ultimi 'count' posti con 1
    for i in range(len(L) - count, len(L)): #dalla pos del primo 1 fino alla fine metto 1
        L[i] = 1
    
    return L

#costo: O(n)

L=[1,1,0,1,1,0,1,1,1,0,0,0]
print(binord(L))

# In[]

def sort_binary_list(a):
    """
    l'idea è la seguente: sia z il numero di zeri in a.
    Allora è sufficiente modificare la lista inserendo 0
    nelle prime z posizioni e inserendo 1 nelle ultime
    len(a)-z posizioni
    """
    z = 0
    for e in a:
        if e == 0:
            z += 1
    k = 0
    while z:
        a[z] = 0
        z = z - 1
        k = k + 1

    for j in range(k, len(a)):
        a[j] = 1


"""
Complessità temporale: O(n)
Complessità spaziale: O(1)
"""


a = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

print("Input: ", a)
sort_binary_list(a)
print("Output: ", a)

"""
oppure usa:
    def sort_binary_list(a):
    """
    """
    idea è la seguente: sia z il numero di zeri in a.
    Allora è sufficiente modificare la lista inserendo 0
    nelle prime z posizioni e inserendo 1 nelle ultime
    len(a)-z posizioni
    """
    """
    count = 0
    for i in a:
        if i == 0:
            count += 1
    i = 0
    while i<count:
        a[i] = 0
        i+=1

    for j in range(i, len(a)):
        a[j] = 1
    
    return a


"""
Complessità temporale: O(n)
Complessità spaziale: O(1)
"""

a = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
print(sort_binary_list(a))
"""



# In[]

"""
Scrivere una funzione in Python che, date due liste l1 e l2 entrambe ordinate, restituisce una lista che è l'intersezione delle due
liste l1 e l2. La soluzione deve avere complessità temporale lineare in len(l1) + len(l2), e memoria supplementare costante,
possibilmente.

Nota: considerate le liste come insiemi, ovvero, non ci sono elementi ripetuti.
"""

a =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
b =  [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]
c=[]

i, j=0, 0

while i<len(a) and j<len(b):
    if a[i]==b[j]:
        c.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1
    else:
        j+=1
        
print(c)

# In[]

"""
Scrivere una lambda function che prenda una stringa e restituisce True se la stringa è palindroma, False altrimenti;
"""

a=lambda x: True if x==x[::-1] else False
print(a("girafarig"))

# In[]

"""
Scrivere una lambda function che prenda una lista di tuple e restituisca una lista di tuple ordinate per il secondo elemento di
ciascuna tupla;
"""

a=lambda x: sorted(x, key=lambda t: t[1])
L=[(1,2),(2,1),(4,3)]
print(a(L))

# In[]

"""
Scrivere una funzione in Python che, date due liste l1 e l2 entrambe ordinate, restituisce una lista che è la differenza delle due
liste l1 e l2, ovvero, la nuova lista deve contenere tutti gli elementi di l1 tranne quelli che sono presenti anche in l2.
La soluzione deve avere complessità temporale lineare in len(l1) + len(l2), e memoria supplementare costante, possibilmente.

Nota: considerate le liste come insiemi, ovvero, non ci sono elementi ripetuti.
"""

def difference_sorted(l1,l2):
    result = []
    n, m = len(l1), len(l2)
    i, j = 0, 0
    while i < n and j < m:
        if l1[i] == l2[j]:
            i += 1
            j += 1
        elif l1[i] < l2[j]: #se l1[i]<l2[j] vuol dire che l1[i] non è in l2[j] perchè stiamo trattando liste ordinate
            result.append(l1[i])
            i += 1
        else:
            j += 1

    while i < n: #questo perchè una delle sue liste terminerà prima e quindi bisogna aggiungere i restanti elementi di l1
        result.append(l1[i])
        i+=1
        
    return result

"""
Complessità temporale: O(n+m), dove n = len(l1) e m = len(l2)
Complessità spaziale: O(1)
"""

l1 = [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 = [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]

print("Output: ", difference_sorted(l1, l2))

# In[]

def union_sorted(l1, l2):
    result = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            result.append(l1[i])  # Aggiungi l'elemento se è uguale in entrambe le liste
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])  # Aggiungi l'elemento da l1
            i += 1
        else:
            result.append(l2[j])  # Aggiungi l'elemento da l2
            j += 1

    # Aggiungi gli elementi rimanenti di l1, se ce ne sono
    while i < len(l1):
        result.append(l1[i])
        i += 1

    # Aggiungi gli elementi rimanenti di l2, se ce ne sono
    while j < len(l2):
        result.append(l2[j])
        j += 1

    return result

l1 = [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 = [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]

print("Output: ", union_sorted(l1, l2))

# In[]

"""
Scrivere una funzione in Python che, date due liste l1 e l2 entrambe ordinate, effettua l'operazione di merge in loco, ovvero senza
costruire una nuova lista. In particolare, se len(l1) = n e len(l2) = m, allora la funzione deve scrivere in l1 i primi n elementi
più piccoli e in l2 gli elementi rimanenti.
"""

def merge(a, b):

    c=[]

    i, j = 0, 0

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
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
        
    i=0
    for e in c[:len(a)]:
        a[i]=e
        i+=1
        
    j=0
    for x in c[len(a):]:
        b[j]=x
        j+=1
        
    print(a+b)

a = [1, 4, 7, 8, 10]
b = [2, 3, 9]
merge(a, b)

# In[]

def mergeloco(a, b):
    i = j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    # Sovrascrivi solo ciò che serve
    for i in range(len(a)):
        a[i] = c[i]
    # Riscrivi solo i necessari in b
    for j in range(len(c) - len(a)):
        if j < len(b):
            b[j] = c[len(a) + j]
        else:
            b.append(c[len(a) + j])
    # Tronca b se è troppo lunga
    while len(b) > len(c) - len(a):
        b.pop()

    return a + b

a = [1, 4, 7, 8, 10]
b = [1, 2, 3, 9]
print(mergeloco(a, b))

# In[]

"""
Scrivere una funzione in Python che, dato un dizionario d con all'interno coppie del tipo (key, list[int]),
crea un dizionario con coppie del tipo (sum(list[int]), key).
"""

def dcoppiadiz(d):
    
    new_diz={}
    for k,v in d.items():
        new_diz[sum(v)]=k        
        
    return new_diz
d={'a': [2, 4, 5, 7], 'b': [6, 2, 4, 5], (2, 'A'): [4, 5, 6]}
print(dcoppiadiz(d))

# In[]

def inverti_dizionario(d):
    return {v: k for k, v in d.items()}

d = {'a': 1, 'b': 2, 'c': 3}
print(inverti_dizionario(d))

#inverte il dizionario in loco
