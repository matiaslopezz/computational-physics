# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:14:47 2020
Autor: Matías López

Este programa calcula los 100 primeros números de la secuencia de Fibonacci.

"""

def fibonacci(n):
    a = 0
    b = 1
    
    while a < n:
        print(a)
        c = a + b
        a = b
        b = c
    print()
    
fibonacci(100)
