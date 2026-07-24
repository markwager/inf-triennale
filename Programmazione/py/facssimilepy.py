"""
scrivere una funzione deep_mean che prenda in input una lista e ritorna la media dei numeri in essa conetenuti a qualsiasi profondit√ .
"""

def deep_mean(L):
    count=0
    for i in L:
        if type(i)!=list:
            count+=i
        else:
            count+=deep_mean(i)
    return count/len(L)


L=[1,2,3,[4,5],6,7,8,9]
print(deep_mean(L))

#la complessit√  temporale di questa funzione √® O(n) perch√® se ci riferissimo visivamente a una struttura ad albero per n elementi dove, tra questi ci sono liste annidate e le 
#"scoppiamo", allora gli elementi interni sono proprio n.

# In[]

def deep_mean(L):
    somma = 0
    ct = 0
    for i in L:
        if type(i) != list:
            somma += i
            ct += 1
        else:
            s, c = deep_mean(i)
            somma += s
            ct += c
    return (somma, ct)

L = [1, 2, 3, [4, 5], 6, 7, 8, 9]
s, c = deep_mean(L)
print(s / c)  # Output: 5.0