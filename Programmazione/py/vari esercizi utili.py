#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:32:44 2025

@author: valerio
"""

def roman_to_int(stringa):
    diz = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    totale = 0
    prev = 0  # Per tenere traccia del valore precedente nel ciclo

    for i in range(len(stringa)):
        if stringa[i] in diz.keys():  # Controlla se il carattere è una chiave del dizionario
            valore = diz[stringa[i]]
            if valore > prev:  # Se il valore corrente è maggiore del precedente, sottrai il precedente e aggiungi la differenza
                totale += valore - 2 * prev
            else:  # Altrimenti somma semplicemente il valore
                totale += valore
            prev = valore  # Aggiorna il valore precedente per il prossimo ciclo

    return totale

stringa = "XIV"
print(roman_to_int(stringa))  # Output: 14

# In[]

def sono_anagrammi(stringa1, stringa2):
    lista_minuscola1 = []
    lista_minuscola2=[]
    for char1 in stringa1:
        lista_minuscola1.append(char1.lower())  # Converti ogni carattere in minuscolo
        
    lista_minuscola1.sort()
    stringa_minuscola1 = ''.join(lista_minuscola1)
    
    
    for char2 in stringa2:
        lista_minuscola2.append(char2.lower()) # Converti ogni carattere in minuscolo
    lista_minuscola2.sort()

    stringa_minuscola2 = ''.join(lista_minuscola2) 

    
    if stringa_minuscola1==stringa_minuscola2:
        return True
    return False
        

stringa1="Ascolta"
stringa2="Calosta"
print(sono_anagrammi(stringa1, stringa2))

# In[versione migliore]

def anagrammi(str1,str2):
    x=str1.lower()
    y=str2.lower()
    
    list1=list(x)
    list2=list(y)
    
    list1.sort()
    list2.sort()
    
    stringa1="".join(list1)
    stringa2="".join(list2)
    
    if stringa1!=stringa2:
        return False
    return True

str1="Ascolta"
str2="Calota"
print(anagrammi(str1,str2))

# In[]

def rimuovi_duplicati(lista):
    
    d={}
    for i in lista:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    return [k for k,v in d.items() if v==1]
        

lista=[1, 2, 3, 2, 1, 4]
print(rimuovi_duplicati(lista))  # Output: [1, 2, 3, 4]

# In[]

def filtra_primi(L):
    def is_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):  # Controlla divisori fino alla radice quadrata di n
            if n % i == 0:
                return False
        return True
    
    lista=[]
    for i in L:
        if is_primo(i):
            lista.append(i)
    return lista


L=[10, 3, 5, 6, 7, 8]
print(filtra_primi(L))  # Output: [3, 5, 7]

# In[]

def nprimi(L):
    
    for x in L:
        n=1
        count=0
        while(n<=x):
            if x%n==0:
                count+=1
            n+=1
        if count==2:
            print(x)

L=[1,2,3,4,5,6,7,8]
nprimi(L)

# In[]

def crea_matrice(r,c,n):
    
    matrice = []
    
    for i in range(r):
        riga = [n] * c  # Crea una nuova riga con `c` elementi uguali a `n`
        matrice.append(riga)  # Aggiungi la nuova riga alla matrice

    return matrice

r=3
c=4
n=0

print(crea_matrice(r, c, n))

# In[]

def conta_vocali(stringa):
    
    d={}
    stringa1="".join(stringa.split()) #mi riunisce le parole della stringa
    lista=[]
    for i in stringa1:
        lista.append(i.lower())
    stringafinale="".join(lista)
    print(stringafinale)
    
    count=0
    for i in stringafinale:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    for k,v in d.items():
        if k=='a' or  k=='e' or k=='i' or  k=='o' or k=='u':
            count+=1
    return count

stringa="Ciao Mondo"
print(conta_vocali(stringa))  # Output: 4

# In[]

def massimo_prodotto(L):
    
    massimo1=max(L)
    lista=[]
    
    lista.append(massimo1)
    
    indice = 0
    for i in range(len(L)):
        if L[i] != massimo1:
            L[indice]=L[i]
            indice+=1
   
    del(L[-1])
    
    massimo2=max(L)
    
    lista.append(massimo2)
    
    indice = 0
    for i in range(len(L)):
        if L[i] != massimo2:
            L[indice]=L[i]
            indice+=1
    #ti elimina il massimo in mezzo alla lista rimettendo i valori
    #giusti nella lista fintanto che so diversi, se 4==massimo -> rimpiazzato con elemento successivo
   
    del(L[-1])
    
    return lista[0]*lista[1]


L=[1, 3, 4, 2]
print(massimo_prodotto(L))  # Output: 12 (3 * 4)

# In[]

def somma_cifre(nums):
    somma=0
    stringa=str(nums)
    stringa=",".join(stringa)
    print(stringa)
    L=[]
    
    for i in stringa:
        if i!=',':
            num=int(i)
            L.append(num)
    
    for j in L:
        somma+=j
            
    return somma
    
nums=123
print(somma_cifre(nums))  # Output: 6 (1 + 2 + 3)

# In[]

def inverti_parole(frase):
    # Suddividi la frase in una lista di parole usando lo spazio come separatore
    parole = frase.split()
    
    # Inverti la lista di parole
    parole_invertite = parole[::-1]
    
    # Unisci di nuovo le parole in una stringa con uno spazio tra di esse
    frase_invertita = " ".join(parole_invertite)
    
    return frase_invertita

# Esempio di utilizzo:
print(inverti_parole("Ciao come stai"))  # Output: "stai come Ciao"

# In[]
#fare un'unione dei valori in base alle chiavi e poi un'unione globale
def unionediz(dizionari):
    
    unione_per_chiave = {}
    
    # Calcola l'unione per ciascuna chiave
    for dizionario in dizionari:
        for k, insieme in dizionario.items():
            # Se la chiave non esiste nel dizionario unione_per_chiave, inizializziamo la lista
            if k not in unione_per_chiave:
                unione_per_chiave[k] = []
    
            for i in insieme:
                if i not in unione_per_chiave[k]:
                    unione_per_chiave[k].append(i)
        
    return unione_per_chiave


dizionari = [
    {'A': {1, 2, 3}, 'B': {4, 5}},
    {'A': {2, 3, 6}, 'B': {1, 7}},
    {'A': {1, 4}, 'B': {2, 5, 6}}
]
print(unionediz(dizionari))

# In[]

def intersez(d1,d2):

    d={}
    for k,v in d1.items():
        if k not in d:
            d[k]=[]
        for i in v:
            if i not in d[k]:
                d[k].append(i)
                       
    for k1,v1 in d2.items():
        if k1 not in d:
            d[k1]=[]
            
        for i in v1:
            if i not in d[k1]:
                d[k1].append(i)
            
    return d


d1 = {'A': {1, 2, 3}, 'B': {4, 5}}
d2 = {'A': {2, 3, 6}, 'B': {1, 7}, 'C': {1, 7}}

print(intersez(d1, d2))

# In[]

def intersez(d1,d2):
    
    d={}
    for k,v in d1.items():
        if k not in d:
            d[k]=[]
    for k1,v1 in d1.items():
        if v1 not in d[k1]:
            d[k1].append(v1)
                       
    for k2,v2 in d2.items():
        if k2 not in d:
            d[k2]=[]
            
    for k3,v3 in d2.items():
        if v3 not in d[k3]:
            d[k3].append(v3)
            
    return d


d1 = {'A': {1, 2, 3}, 'B': {4, 5}}
d2 = {'A': {2, 3, 6}, 'B': {1, 7}, 'C': {1, 7}}

print(intersez(d1, d2))

# In[]

def differenza_insiemi(dizionario1, dizionario2):
    differenza_per_chiave = {}

    # Calcoliamo la differenza per ogni chiave
    for chiave in dizionario1:
        if chiave in dizionario2:
            differenza_per_chiave[chiave] = {}
            for elemento in dizionario1[chiave]:
                if elemento not in dizionario2[chiave]:
                    differenza_per_chiave[chiave][elemento] = True
        else:
            # Se la chiave non è presente nel secondo dizionario, prendiamo tutto
            differenza_per_chiave[chiave] = {}
            for elemento in dizionario1[chiave]:
                differenza_per_chiave[chiave][elemento] = True

    return differenza_per_chiave

# Esempio di uso
dizionario1 = {'A': {1, 2, 3}, 'B': {4, 5}}
dizionario2 = {'A': {2, 3, 6}, 'B': {1, 7}}

risultato = differenza_insiemi(dizionario1, dizionario2)
print(risultato)

# In[]

def unionediz(l1, l2):
    d = {}  
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:  # Se gli elementi sono uguali, aggiungilo una volta sola
            d[l1[i]] = True
            i += 1
            j += 1
        elif l1[i] < l2[j]:  # Aggiungi l'elemento minore
            d[l1[i]] = True
            i += 1
        else:
            d[l2[j]] = True
            j += 1

    # Aggiungi gli elementi rimanenti di l1
    while i < len(l1):
        d[l1[i]] = True
        i += 1

    # Aggiungi gli elementi rimanenti di l2
    while j < len(l2):
        d[l2[j]] = True
        j += 1
        
    c=[k for k,v in d.items()]

    return c

l1 = [1, 2, 3, 4]
l2 = [1, 3, 5, 8, 9]
print(unionediz(l1, l2))  
# Output: {1: True, 2: True, 3: True, 4: True, 5: True, 8: True, 9: True}

# In[]

def intersezionediz(l1, l2):
    d = {}
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:  # Elemento comune
            d[l1[i]] = True
            i += 1
            j += 1
        elif l1[i] < l2[j]:  
            i += 1
        else:
            j += 1

    return d


l1 = [1, 2, 3, 4]
l2 = [1, 3, 5, 8, 9]
print(intersezionediz(l1, l2))  
# Output: {1: True, 3: True}

# In[]

def differenzadiz(l1, l2):
    d = {}
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:  # Se è in entrambi, lo ignoriamo
            i += 1
            j += 1
        elif l1[i] < l2[j]:  # Aggiungiamo elementi solo da l1
            d[l1[i]] = True
            i += 1
        else:
            j += 1

    # Aggiungiamo eventuali elementi rimanenti di l1
    while i < len(l1):
        d[l1[i]] = True
        i += 1

    return d


l1 = [1, 2, 3, 4]
l2 = [1, 3, 5, 8, 9]
print(differenzadiz(l1, l2))  
# Output: {2: True, 4: True}
