#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:43:21 2024

@author: valerio
"""
a=input("Scrivi qualcosa: ")
i=0
count=0
flag=False
while(i<len(a)):
    flag=False
    while(a[i]==' ' and flag==False):
       count=count+1
       flag=True
    i=i+1
print(count)

# In[v. 2.0]

a=input("Scrivi qualcosa: ")
i=0
count=0

while(i<len(a)):
    if(a[i]==' '):
       count=count+1
    i=i+1
print(count)



# In[nuova versione]

a=input("Scrivi qualcosa: ")
i=0
count=0
while(i<len(a)):
    if(a[i] in 'aeiou'):
       count=count+1
    i=i+1
print(count)

#potrei metterci un flag al posto dell'if