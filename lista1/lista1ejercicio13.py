# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:24:43 2020
Autor: Matías López

Este progrma calcula lo siguiente:
1. la suma de elementos de una progresión aritmética dados el primer
término i_0, la razón k y el número de elementos n.
2. el factorial de un número entero positivo k.
3. el número de combinaciones de m elementos tomados de n.
4. la precisión de la máquina  e  entendida como el número más chico
que sumado a 1 da un resultado distinto de 1.

"""
#Parte 1
i = int(input("Ingrese el primer término: i = "))
k = int(input("Ingrese el paso de la serie: k = "))
n = int(input("Ingrese los elementos de la serie: n = "))

suma = (n*(2*i+(n-1)*k))/2
print("La suma de los elementos de la serie es: ", suma)

#Parte 2
k = int(input("Ingrese un número k = "))

def factorial(k):
    n = 1
    for i in range(1,k+1):
        n *= i
    
    return n

print(factorial(k))

#Parte 3
n = int(input("Ingrese un número m = "))
m = int(input("Ingrese un número n = "))

def combinatoria(m,n):
    factorial_m = factorial(m)
    factorial_n = factorial(n)
    factorial_resta = factorial(n-m)
    
    comb = factorial_n/(factorial_m*factorial_resta)
    
    return comb

print(combinatoria(m,n))

#Parte 4

def precision():
    paso = 1
    while paso+1 != 1:
        paso *= 0.1
    return paso

print(precision())
