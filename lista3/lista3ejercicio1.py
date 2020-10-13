# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:41:56 2020
Autor: Matías López
"""

def f(x):
    return x**4 - 2*x**2 + 1

# ----- Parte (a) ----- #
#Regla trapezoidal extendida
N = 10
a = 0.0
b = 2.0
h = (b-a)/N
s = 0.5*f(a) + 0.5*f(b)

for k in range(1,N-1):
    s += f(a + k*h)
    int_trapezoidal = h*s
    
print("Resultado por regla trapezoidal: ", int_trapezoidal) #devuelve 2.92704

#Resolución analítica
from sympy import symbols
from scipy.integrate import quad

x = symbols('x')
int_analitic = quad(f, 0, 2)

print("Resultado analítico: ", int_analitic[0]) #devuelve 3.066

#Error
error = (int_analitic[0]-int_trapezoidal)/int_analitic[0]
print("Error fraccional: ", error,"\n")

# ----- Parte (b) ----- #
#Regla de Simpson extendida
N = 10
a = 0.0
b = 2.0
h = (b-a)/N

s1 = 0
for i in range(1,N,2):
    s1 += 4*f(a + i*h)

s2 = 0
for j in range(2,N,2):
    s2 += 2*f(a + j*h)
    
int_simpson = (h/3)*(f(a) + f(b) + s1 + s2)
print("Resultado por regla de Simpson: ", int_simpson, "\n") #devuelve 3.067

#Tiene una diferencia con al regla trapezoidal de 0.924; la regla de Simpson
#da un resultado mucho más acertado que la regla trapezoidal.


# ----- Parte (c) ----- #
def integrate(f, a, b, method, N):
    h = (b-a)/N
    
    if method == "trapezoidal":
        s = 0.5*f(a) + 0.5*f(b)
        for k in range (1,N-1):
            s += f(a + k*h)
        trap = h*s
        return trap
    
    elif method == "simpson":
        s1 = 0
        for i in range(1,N,2):
            s1 += 4*f(a + i*h)
            
        s2 = 0
        for j in range(2,N,2):
            s2 += 2*f(a + j*h)
        
        simp = (h/3)*(f(a) + f(b) + s1 + s2)
        return simp
    
    else: 
        print("No eligió ningún método")
        
result = integrate(lambda x: x**4 - 2*x**2 + 1, 0, 2, "trapezoidal", 10)
print("El resultado con el método elegido es: ", result, "\n")

# ----- Parte (d) ----- #
import numpy as np
from pylab import plot,title,xlabel,ylabel,legend,show

N = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
int_t = []
int_s = []

for i in N:
    t = integrate(lambda x: x**4 - 2*x**2 + 1, 0, 2, "trapezoidal", i)
    int_t = np.append(int_t,t)
    s = integrate(lambda x: x**4 - 2*x**2 + 1, 0, 2, "simpson", i)
    int_s = np.append(int_s,s)
    
plot(N,int_t, "r", label = "Trapezoidal")
plot(N,int_s, "y", label = "Simpson")
title("Trapezoidal vs Simpson")
xlabel("N")
ylabel("Integral result")
legend(loc ="lower right")
show()

"""

Vemos que la regla trapezoidal arroja resultados más exactos cuanto mayor sea
el número N, mientras que la regla de Simpson se mantiene próxima al valor
real de la integral aún para N pequeños.

"""


    
    