# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:35:53 2020
Autor: Matías López

"""
#Usando la ley de kirchhoff (la suma de la corriente en un nodo vale cero) y 
#la ley de Ohm, las ecuaciones a resolver son
#(V1-V)/R + (V1-V3)/R + (V1-V4)/R + (V1-V2)/R = 0
#(V3-V)/R + (V3-V1)/R + (V3-V4)/R = 0
#(V2-V1)/R + (V2-V4)/R + (V2-0)/R = 0
#(V4-V3)/R + (V4-V1)/R + (V4-V2)/R + (V4-0)/R = 0
#Con V = 5

from numpy.linalg import solve
from numpy import array

A = array([[4,-1,-1,-1],[-1,0,3,-1],[-1,3,0,-1],[-1,-1,-1,4]], float)
v = array([5,5,0,0], float)

x = solve(A,v)
print("x = ", x)
