# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:01:34 2020
Autor: Matías López

Entrada: variable i
Salida: valores que toma la variable i dentro del bucle

Este programa imprime lo siguiente usando el comando *for*:
    prints 2
    prints 4
    prints 6
    prints 8
    prints 10
    prints Goodbye!

"""

for n in range(2,11,2):
    print(n)
    
    if n == 10:
        print("Goodbye!")

#print("Goodbye!")