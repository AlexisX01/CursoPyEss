# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:38:57 2022
Programa de numeros primos
@author: Alexis Criollo

"""
def isPrime(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    
    for var in range(2,numero,1):
        if numero%var == 0:
           return False
    return True
    

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
