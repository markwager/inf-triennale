#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:42:27 2025

@author: valerio
"""

def deep_mean(L):
    media = 0
    count = 0
    
    for i in L:
        if type(i) == int:
            media += i
            count += 1
        elif type(i) == list or type(i) == tuple:
            sub_media, sub_count = deep_mean(i)  
            media += sub_media
            count += sub_count
    
    return media, count  

L = [1, 2, 3, [4, 5, 7, [1, 1, 1]], 1, [12]]

media, count = deep_mean(L)
print(media / count if count != 0 else 0)