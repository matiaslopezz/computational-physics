# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:45:15 2020
Autor: Matías López

Entrada: string -s-
Salida: número de vocales en s

Este programa cuente el número de vocales contenidas en una string dada.

"""

s = (input("Ingrese una palabra en minúsculas: "))

def conteoVocales(string):
    vocales = 'aeiou'
    contador = 0
    
    for aux in string:
        if aux in vocales:
            contador += 1
    
    print(contador)

print("El número de vocales en s es: ")
conteoVocales(s)

