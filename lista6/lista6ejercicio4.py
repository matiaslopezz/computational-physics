# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:03:12 2020
Autor: Matías López

"""

#Ejercicio 4

# ----- Parte (a) ----- #

from numpy import array,arange
from pylab import plot,xlabel,ylabel,legend,title,show

#Defino los parámetros
r = 28
sigma = 10
b = 8/3

t_inicial = 0
t_final = 50
N = 20000
h = (t_final - t_inicial)/N

tpoints = arange(t_inicial,t_final,h)
xpoints = []
ypoints = []
zpoints = []

def f(R,t):
    x = R[0]
    y = R[1]
    z = R[2]
    fx = sigma * (y - x)
    fy = r * x - y - x * z
    fz = x * y - b * z
    return array([fx,fy,fz],float)

x_0 = 0
y_0 = 1
z_0 = 0
R = array([x_0,y_0,z_0],float)

for t in tpoints:
    xpoints.append(R[0])
    ypoints.append(R[1])
    zpoints.append(R[2])
    k1 = h * f(R,t)
    k2 = h * f(R + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(R + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(R + k3, t + h) 
    R += (k1 + 2 * k2 + 2 * k3 + k4)/6

# ----- Parte (b) ----- #
print("# ----- Parte (b) ----- #","\n")

plot(tpoints, xpoints, label = "x(t)")
plot(tpoints, ypoints, label = "y(t)")
plot(tpoints, zpoints, label = "z(t)")
xlabel("Time (s)")
legend()
show()

plot(xpoints,zpoints, "y")
xlabel("x")
ylabel("z")
title("Lorentz attractor")
show()

    
    
    
    
    
    
    
    
    
    
    