#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:30:04 2024

@author: valerio
"""
#enumerazione esaustiva: enumeriamo tutte le possibilità finché non arriviamo alla risposta giusta,
#`oppure esauriamo lo spazio delle possibilità
x=int(input("Inserisci numero: "))
ans=0
while ans**3<abs(x):
    ans+=1
if ans**3!=abs(x):
    print(x,"non è un cubo perfetto")
else:
    if x<0:
        ans=-ans
    print("la radici cubica di",x,"è", ans)
    
# In[]
x=int(input("Inserisci un numero: "))
root=0
flag=False
for pwr in range(2,6):
    while (-abs(x)<root**pwr<abs(x)):
        root+=1
        if(root**pwr==x):
            print(root,pwr)
            
# In[]

 # Verifica se un int > 2 è primo. Se non lo è, stampa
# il più piccolo dei suoi divisori
x = int(input('Inserisci un intero maggiore di 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Il più piccolo divisore di', x,'è', smallest_divisor)
else:
    print(x, 'è un numero primo')
            
            
# In[]

prime_sum = 0

# Iteriamo solo sui numeri dispari da 3 a 999
for num in range(3, 1000, 2):
    # Verifica se il numero è primo fino alla sua radice quadrata
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    # Se il numero è primo, aggiungilo alla somma
    if prime==True:
        prime_sum += num

print("La somma dei numeri primi maggiori di 2 e minori di 1000 è:", prime_sum)
        
# In[]
#approssimazione della radice quadrata
x=int(input("Inserisci un num per il quale si calcola la radice quadrata: "))
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1
print('numero di congetture =', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Non ho trovato la radice quadrata di', x)
else:
    print(ans, 'è vicino alla radice quadrata di', x)
    
# In[]

#ricerca dicotomica permette di avere un algortimo più efficinete di quello di sopra
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print('basso =', low, 'alto =', high,  'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('numero di congetture =', num_guesses)
print(ans, 'è vicino alla radice quadrata di', x)
       


        
   
    
    
    
    