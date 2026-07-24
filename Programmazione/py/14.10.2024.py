#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 08:27:58 2024

@author: valerio
"""
a= 'programmazione dei calcolatori'
i=4
spaces_from_i=0
j=i

while(a[j]==' '):
    spaces_from_i+=1
    j+=1
print(spaces_from_i)

# In[]

a=' prpogrammazione dei caloclatori '
i=4
spaces_from_i=0
#j=i

while(a[spaces_from_i]==' ' and a[i+spaces_from_i<len(a)]==' '):
    spaces_from_i+=1
    #j+=1
print(spaces_from_i)

# In[]
a=' prpogrammazione dei caloclatori '
i=4
spaces=0
spaces_from_i=0
while(i+spaces_from_i<len(a) and a[i+spaces_from_i]==' '):
    spaces_from_i+=1
    spaces+=spaces_from_i
    i+=spaces_from_i+1
print(spaces)
    
# In[]

a='ciao'

for x in a: #per ogni char in a
    if(x in 'aeiou'):
        print(x)

# In[]

a='cia0 sono v4ll1'
b=''

#stampa a ed evidenziare con asterisco le vocali e con cancelletto le cifre decimali

for x in a:
    if(x in 'aeiouAEIOU'):
        b+='*'
    elif(x in '1234567890'): #questa è un'operazione non scalare(composta), cioè composta da più operazioni scalari(elementari) #fa 10 controlli #x>=0 and x<=9 è più efficiente perchè ci sono solo due operazioni scalari)
        b+='#'
    else:
        b+=' '
print(a)
print(b)
#algoritmo efficiente: riesce a minimizzare il numerori di operazioni elementari (o elementari)
#op.aritm:scalari, op.assegnamneto:scalare, confronto tra booleani: scalari
 

# In[]

'a'>'1'
'a'>'A'
print(ord('a')) #char->ord.less.graf
print(chr(100)) #ord.less.graf->char