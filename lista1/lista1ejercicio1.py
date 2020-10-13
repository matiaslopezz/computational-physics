# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:57:28 2020
Autor: Matías López

Entradas: r,theta
Salidas: x,y

Esta función trasnforma las coordenadas polares ingresadas por el usuario
en sus respectivas coordenadas cartesianas.

"""
from math import cos,sin,pi

r = float(input("Ingrese la coordenada r: "))
a = float(input("Ingrese el ángulo theta en grados: "))
theta = a*pi/180
'\n'

def polarToCartesian(r,theta):
   x = r*cos(theta) 
   y = r*sin(theta)
   position = [x,y]
   return position

print("x = " + str(polarToCartesian(r, theta)[0]))
print("y = " + str(polarToCartesian(r, theta)[1]))

