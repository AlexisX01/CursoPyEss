# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:02:38 2022

@author: Usuario
"""

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break