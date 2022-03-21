# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:32:43 2019

@author: Juan Carlos
"""
def fib(n):
    a=0
    b=1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
    print("\n"*2)
#fib(8)   
