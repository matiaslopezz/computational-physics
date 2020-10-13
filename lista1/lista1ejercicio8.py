# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:14:22 2020
Autor: Matías López

Entradas: varA y varB
Salidas: mensajes

A partir de dos variables (varA y varB), que pueden ser números o cadenas
de caracteres, el programa evalúa estas variables e imprime los siguientes
mensajes:

."string involved": si una de las variables varA o varB es un string
."bigger": si varA es mayor que varB
."equal": si varA es igual varB
."smaller": si varA es menor que varB

"""

#varA = input("Ingrese un número entero o una string: varA = ")
#varB = input("Ingrese un número entero o una string: varB = ")

varA = "varA"
varB = 5

if type(varA) == str or type(varB) == str:
    print("string involved")


if type(varA) == int and type(varB) == int:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")

