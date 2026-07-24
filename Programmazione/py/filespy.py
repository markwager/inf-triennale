#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:58:40 2025

@author: valerio
"""

nome_file = 'rosalinda.txt'

f = open(nome_file,'r')
righe=f.readlines() #ritorna lista con righe
f.close()


i=1

out=open("output_rosa.txt",'w')

for riga in righe:
    if i%2==0:
        print(riga)
        out.write(riga)
    i+=1
out.close()
