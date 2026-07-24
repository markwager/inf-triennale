#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:56:47 2024

@author: valerio
"""

num_x = int(input('Quante volte devo stampare la X?'))
to_print = ''
# concatena X a to_print per num_x volte
i=0
while(i<num_x):
    to_print='X'*num_x
    i=i+1
print(to_print)

# In[]

#Scrivete un programma che chieda all’utente di inserire 10 interi e poi stampi il numero dispari più grande fra quelli inseriti.
#Se non è stato inserito alcun numero dispari, deve stampare un messaggio che lo dica esplicitamente.
flag=False
i=0
ris=0
while(i<10):
    x=int(input("Inserisci un numero: "))
    if(x%2!=0):
        if (x>ris):
            ris=x
    else:
        flag=True
    i=i+1
    
if (flag==False):
    print("Numeeo dispari inserito più grande è", ris)
else:
    print("Non sono stati inseriti numeri dispari")

    

    