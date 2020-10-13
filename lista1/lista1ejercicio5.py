# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:52:15 2020
Autor: Matías López

Entradas: contador n, valor inicial c y array a completar con los números
de Catalán menores a un billón.
Salidas: array con los números de Catalán correspondientes

Este programa devuelve los números de Catalan menores a un billón.

"""
import numpy as np

c = 1
n = 0

c_n = c*((4*n+2)/(n+2))

serie = np.append(c,c_n)

while (c_n <= 10e12):
    n += 1
    c = c_n
    c_n = c*((4*n+2)/(n+2))
    serie = np.append(serie,c_n)
   
    
print("Los números de Catalan menores a 10e12 son:"'\n')
print(serie)


print('\n'"El último número menor a un billón es: ", c_n)
