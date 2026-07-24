#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:31:06 2024

@author: valerio
"""

a=input("Scrivi prima stringa: ")
b=input("Scrivi seconda stringa: ")
flag=False
for x in a:
    if (x in b):
        print(x)
        

# In[]

def perfect_numb(a):
    i=1
    numeri=0
    a=int(input("Inserisci un numero: "))
    while i<a:
        if(a%i==0):
            numeri=i
            i+=1
            print(numeri)
        else:
            i+=1
    return numeri

# In[]

a=input("Inserisci stringa: ")
b=''
i=0
while i<len(a):
    b+=chr(ord(a[i])+13)
    i+=1
print(b)
