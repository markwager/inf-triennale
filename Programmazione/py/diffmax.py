#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 16:11:11 2025

@author: valerio
"""

def massimo(L):
    diffmax=L[0]
    for i in range(1, len(L)):
        diff = L[i] - L[i - 1]
        if diffmax>diff:
            diffmax=diff
    return diffmax

L=[1,5,3,9,2]
print(massimo(L))