"""
Si scriva una funzione in py chiamata mode che prende in input una lista di numeri e restituisca la lista degli elementi di a che compaiono pià frequentemenete
"""

def mode(L):
    numeri=[]
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]==L[j] and L[i] not in numeri:
                numeri.append(L[i]) 

    return numeri

L=[1,2,6,9,1,4,6,2,3,1,9,7,6]
print(mode(L))