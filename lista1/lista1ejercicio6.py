# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:37:06 2020
Autor: Matías López

Entrada: archivo de texto plano con datos numéricos a calcular su promedio.
Salida: array con los datos (data) y el valor medio (mean).

Este programa lee un conjunto de datos guardados en un archivo llamado
datos.txt, calcula e imprime el valor medio.

"""
from numpy import loadtxt

data = loadtxt("datos.txt",float)
mean = sum(data)/len(data)

print("Los datos del arcivho 'datos.txt' son: ", data)
print("El valor medio de estos datos es: ", mean)