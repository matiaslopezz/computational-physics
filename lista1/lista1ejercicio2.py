# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:32:55 2020
Autor: Matias López

Entradas: x,y
Salidas: r,theta

Esta función trasnforma las coordenadas cartesianas ingresadas por el usuario
en sus respectivas coordenadas polares.

"""

import numpy as np

x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))
print('\n')

def cartesianToPolar(x,y):
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(y,x)
    position = [r,theta]
    return position

print("Las coordenadas polares asociadas son:")
print("r = " + str(cartesianToPolar(x, y)[0]))    
print("theta = " + str(cartesianToPolar(x, y)[1]))
                                  