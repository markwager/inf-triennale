#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:23:13 2025

@author: valerio
"""

def is_matrix(L):
    
    count=0
    for a in range(len(L)+1):
        count=a
        
    ct=count**0.5
    if(count//ct!=ct):
        return False
    
    return True
        

L=[1,2,3,4,5]
print(is_matrix(L))

# In[]

def is_matrix(a):
    count = len(a)
    radq = count ** 0.5
    radice=int(radq)
    
    return radq==radice

L = [1, 2, 3, 4]
print(is_matrix(L))  # Output: False