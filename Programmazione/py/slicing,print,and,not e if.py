# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=input("Inserisci il primo numero ")
y=input("Inserisci il secondo numero ")
z=input("Inserisci il terzo numero ")

a=int(x)
b=int(y)
c=int(z)

if(a%2!=0 and b%2!=0 and a>b):
    if(a%2!=0 and c%2!=0 and a>c):
        print("Il numero dispari più grande è" ,a)
    elif(a%2!=0 and c%2!=0 and a<c):
        print("Il numero dispari più grande è",c)
if(a%2!=0 and b%2!=0 and a<b):
   if(b%2!=0 and c%2!=0 and b>c):
       print("Il numero dispari più grande è" ,b)
   elif(b%2!=0 and c%2!=0 and b<c):
       print("Il numero dispari più grande è",c)
if not(a%2!=0 and b%2!=0 and c%2!=0):
    if(a<b and a<c):
        print("Il numero più piccolo è",a)
    elif(b<a and b<c):
        print("Il numero più piccolo è",b)
    else:
        print("Il numero più piccolo è",c)

# In[]

x=input("Inserisci il primo numero ")
y=input("Inserisci il secondo numero ")
z=input("Inserisci il terzo numero ")

a=int(x)
b=int(y)
c=int(z)

if(a%2!=0 and b%2!=0 and c%2!=0 and a>b and a>c):
    print("Il numero dispari più grande è" ,a)
if(a%2!=0 and b%2!=0 and c%2!=0 and b>a and b>c):
    print("Il numero dispari più grande è" ,b)
if(a%2!=0 and b%2!=0 and c%2!=0 and c>a and c>b):
    print("Il numero dispari più grande è" ,c)

if not(a%2!=0 and b%2!=0 and c%2!=0):
    if(a<b and a<c):
        print("Il numero più piccolo è",a)
    elif(b<a and b<c):
        print("Il numero più piccolo è",b)
    else:
        print("Il numero più piccolo è",c)

# In[]

print(3*'a')
print('a'+'a')
print('abc'[0:3])#legge da a fino a dopo c
print('abc'[0:2])#legge da a fino a b
print('abc'[0])
print('123456789'[0:8:2])
num = 30000000
fraction = 1/2
print(num*fraction, 'is', fraction*100, '%', 'of', num) 
print(num*fraction, 'is', str(fraction*100) + '%', 'of', num)
print(f'{int(num*fraction)} is {fraction*100}% of {num}')#f-stringa

# In[]

x=input("Inserisci la data di nascita in formato gg/mm/aaaa:" )
print("Sei nato nell'anno", x[6:10])

