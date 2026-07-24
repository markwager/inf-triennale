"""
Si scriva una funzione chiamata unique che prende in input una lista di numeri e restituisca una nuova lista contenente solo gli elementi di a che compaiono una sola volta
"""

def unique(L):
    list = []  # Per tenere traccia degli elementi duplicati
    list1 = []  # Per tenere traccia degli elementi che appaiono una sola volta
    l = []  # Lista finale con gli unici

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] == L[j] and L[i] not in list:
                list.append(L[i])  # Aggiungi all'elenco dei duplicati
                
        if L[i] not in list and L[i] not in list1:
            list1.append(L[i])  # Aggiungi l'elemento che non è duplicato alla lista 'list1'

    # Aggiungi gli unici a 'l'
    for x in list1:
        if x not in list:  # Aggiungi gli elementi che appaiono una sola volta
            l.append(x)

    return l

# Test
L = [1, 2, 6, 9, 1, 4, 6, 2, 3, 1, 9, 7, 6]
print(unique(L))  # Output atteso: [4, 3, 7]

# In[]

def unique(L):
    
    d={}
    for i in L:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    return [k for k,v in d.items() if v==1]


# Test
L = [1, 2, 6, 9, 1, 4, 6, 2, 3, 1, 9, 7, 6]
print(unique(L))  # Output atteso: [4, 3, 7]