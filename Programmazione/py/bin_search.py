#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 11:25:21 2025

@author: valerio
"""

def bin_search(n,m,arra,lista):
    
    
    for x in range(m):
        
        lx, rx = 0, n-1
        result = -2  # Valore predefinito se k non è trovato

        while lx <= rx:
            cx = (lx + rx) // 2
            if arra[cx]==lista[x]:
                result=cx
                break
            elif arra[cx] > lista[x]:
             rx = cx - 1
            else:
             lx = cx + 1

        print(result+1,end=" ")
    


n=9449
m=9639
# Inserisci le due liste (es: 10 20 30 40 50)
line1 = input("Inserisci prima lista: ")
print("\n")
line2 = input("Inserisci seconda lista: ")
print("\n")

# Converte in liste di interi
arra = [int(x) for x in line1.strip().split()]
lista = [int(x) for x in line2.strip().split()]
bin_search(n,m,arra,lista)