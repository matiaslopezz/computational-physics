# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:06:22 2020
Autor: Matías López

Entrada: string -s-
Salida: número de veces que aparece 'bob' en s.

El programa cuenta el número de veces que la cadena 'bob' aparece en s.

"""

s = input("Ingrese una palabra en minúsculas: ")

repeticion = s.count('bob')
print("Número de veces que ocurre 'bob': ", repeticion)

"""
#Forma alternativa

s = input("Ingrese una palabra en minúsculas: ")

cadena = 'bob'
repeticion = 0
longitudCadena = len(cadena)

for i in range(len(s)):
    if s[i:i+longitudCadena] == cadena:
        repeticion += 1
print(repeticion)

"""  
