# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:03:08 2020
Autor: Matías López

Entradas: oddInteger (entero impar), evenInteger (entero par)

Este programa pide dos números enteros, uno par y otro impar.
Si el usuario ingresa mal se le permite ingresar nuevamente.
Si los números son correctos se imprimen en pantalla.

"""

oddInteger = int(input("Ingrese un número impar: "))

while oddInteger%2 == 0:
    print(oddInteger, "no es impar")
    oddInteger = int(input("Ingrese un número impar: "))

print(oddInteger, "es impar")

evenInteger = int(input("Ingrese un número par: "))

while evenInteger%2 != 0:
    print(evenInteger, "no es par")
    evenInteger = int(input("Ingrese un número par: "))

print(evenInteger, "es par")
