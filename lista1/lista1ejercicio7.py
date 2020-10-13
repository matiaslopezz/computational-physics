# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:01:28 2020
Autor: Matías López

Entrada: archivo de texto plano con datos numéricos a calcular su promedio.
Salida: array con los datos (data) y el valor medio cuadrático (mean_square).

Este programa lee un conjunto de datos guardados en un archivo llamado
datos.txt, calcula e imprime el valor medio cuadrático.

"""
from numpy import loadtxt
from math import sqrt

data = loadtxt("datos.txt",float)
mean_square = sqrt((sum(data*data))/len(data)) #También funciona con data**2

print("Los datos del arcivho 'datos.txt' son: ", data)
print("El valor medio cuadrático de estos datos es: ", mean_square)
