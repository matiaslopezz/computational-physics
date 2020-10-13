# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:08:37 2020
Autor: Matías López

"""

# ----- Problema 1 ----- #

#Parte (a)
a = int(input("Ingrese un número: a = "))
n = int(input("Ingrese un entero positivo: n = "))

def iterPotencia(a,n):
    resultado = 1
    if n == 0:
        resultado = 1
    else:
        while n >= 1:
            resultado = resultado * a
            n = n - 1
        
    return resultado

print(iterPotencia(a, n))

#Parte (b)
a = int(input("Ingrese un número: a = "))
n = int(input("Ingrese un entero positivo: n = "))

def recurPotencia(a,n):
    if n == 0:
        return 1
    elif n >= 1:
        return a * recurPotencia(a,n-1)

print(recurPotencia(a, n))

# ----- Problema 2 ----- #

#Parte (a)
a = int(input("Ingrese un número: a = "))
b = int(input("Ingrese otro número: b = "))

def iterGcd(a,b):
    divisor = 1
    
    if a % b == 0:
        return b
    
    for k in range(int(b/2), 0, -1): #vamos reduciendo b hasta 1
        if a % k == 0 and b % k == 0: 
            divisor = k #k es el máximo comun divisor para a y b
            break
    
    return divisor

print("El máximo común divisor entre", a,"y", b, "es: ", iterGcd(a, b))

#Parte (b)
a = int(input("Ingrese un número: a = "))
b = int(input("Ingrese otro número: b = "))

def recurGcd(a,b):
    if b == 0:
        return a
    else:
        return recurGcd(b, a % b)

print("El máximo común divisor entre", a,"y", b, "es: ", recurGcd(a, b),"\n")

"""
"Lo que hace el Método de Euclides en detalle:"
    
def recurGcd(a,b):
    resto = 0
    
    while b > 0:
        resto = b
        b = a % b
        a = resto
    
    return a
"""

#Parte (c)
"El método más eficiente es el que realizamos en la parte (a) ya que mediante"
"la forma recursiva siempre vamos a tener que esperar a que se hagan las"
"opreciones intermedias antes de hacer la última y obtener el resultado final."

# ----- Problema 3 ----- #

index = 1
n = 3
while index <= 20:
    contador = 1
    for i in range(2,n):
        if n % i == 0:
            contador += i
    if n == contador:
        print("El", index, "número perfecto es: ", contador)
        index += 1
    n += 1

#ACLARACIÓN:
#Si bien el programa funciona, a partir del 4to número perfecto le toma mucho
#tiempo recorrer el bucle for. No encontré una forma de mejorar la eficiencia.
    
"""
a = int(input("Ingrese un número a chequear si es perfecto: a = "))

def perfectNumber(a):
    contador = 0
    for k in range(1, a):
        if a % k == 0:
            contador = contador + k
    if contador == a:
        print("El número ingresado es perfecto")
    else:
        print("El número ingresado no es perfecto")
        
perfectNumber(a)
"""
