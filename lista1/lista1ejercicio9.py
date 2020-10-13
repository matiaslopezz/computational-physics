# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:56:41 2020
Autor: Matías López

Entrada: variable i
Salida: valores que toma la variable i dentro del bucle

Este programa imprime lo siguiente usando el comando *while*:
    print 2
    prints 4
    prints 6
    prints 8
    prints 10
    prints Goodbye!

"""
i = 0
while i < 10:
    i = i + 2
    print(i)
    
    if i == 10:
        print("Goodbye!")
    
#print("Goodbye!")