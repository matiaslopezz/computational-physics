# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:06:28 2020
Autor: Matías López

"""

#Ejercicio 3

# ----- Parte (a) ----- #

print("# ----- Parte (a) ----- #","\n")
print("En primer lugar la variable x representará las presas y la variable y "
      "a los depredadores.")
print("El término alpha*x representa el crecimiento exponencial de la "
      "población de las presas, y el término beta*x*y representa el encuentro "
      "entre las dos especies, es decir la tasa de muerte.")
print("Por otra parte, el término gamma*x*y hace referencia a la tasa en la "
      "que crecen los depredadores -depende de las presas que comen-, mientras "
      "que el término delta*y representa la muerte de los mismos.","\n")

# ----- Parte (b) ----- #
print("# ----- Parte (b) ----- #","\n")

from numpy import array,arange
from pylab import plot,xlabel,ylabel,legend,show

#Definimos los parámetros a utilizar
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

a = 0.0
b = 30.0
N = 1000
h = (b - a)/N

def f(r,t):
    x = r[0]
    y = r[1]
    fx = alpha * x - beta * x * y
    fy = gamma * x * y - delta * y
    return array([fx,fy], float)

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

x_0 = 2.0
y_0 = 2.0

r = array([x_0,y_0], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h * f(r,t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6

# ----- Parte (c) ----- #
print("# ----- Parte (c) ----- #","\n")

plot(tpoints, xpoints, label = "pray")
plot(tpoints, ypoints, label = "predator")
xlabel("Time (s)")
ylabel("Population in 1000")
legend()
show()