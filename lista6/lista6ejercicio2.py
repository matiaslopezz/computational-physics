# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:33:47 2020
Autor: Matías López

"""

#Ejercicio 2 - Filtro Pasa Bajos

# ----- Parte (a) ----- #

print("# ----- Parte (a) ----- #","\n")
print("Dada la corriente I, la resistencia R, la capacitancia C y la carga Q "
      "tenemos las siguientes relaciones:")
print("IR = V_in - V_out (i)","\n"
      "Q = CV_out (ii)","\n"
      "I = dQ/dt (iii)","\n")
print("Sustituyendo (ii) en (iii) obtenemos: I = C*dV_out/dt "
      "que, sustituyéndolo en (i), se obtiene: dV_out/dt = 1/RC*(V_in - V_out)"
      "\n")

# ----- Parte (b) ----- #

print("# ----- Parte (b) ----- #","\n")
print("Ahora tenemos que V_in es una función cuadrada que vale +1 y -1.")
print("La siguiente función devuelve: V_in.","\n")

from numpy import linspace,floor,arange
from pylab import plot,subplot,show,xlabel,ylabel,title

V = []

def Vin(t,Vo):
    for i in t:
        if floor(2*i) % 2 == 0:
            V.append(Vo)   
        else:
            V.append(-Vo)
    return V
    
t = linspace(0,10,100)
Vo = 1
plot(t,Vin(t,Vo))
xlabel("Tiempo (s)")
ylabel("Período")
title("Función de onda cuadrada para V_in")
show()
print("\n")

# ----- Parte (c) ----- #

print("# ----- Parte (c) ----- #","\n")
print("En esta parte usamos el método RK para integrar la ecuación "
      "dV_out/dt = 1/RC*(V_in - V_out)","\n")

#Declaración deconstantes
Vo = 1  #Valor de la función de onda cuadrada V_in
V0 = 0  #Valor inicial de V_out
a = 0   #Tiempo inicial
b = 10  #Tiempo final
N = 100 #Número de iteraciones
h = (b - a) / N

tpoints = arange(a,b,h)
Vpoints = []
V_in_points = []

RC = 0.01 #0.01, 0.1, 1

def f(RC, t, V0, Vin):
    return (Vin - V0) / RC

i = 0
for t in tpoints:
    
    if floor(2*t) % 2 == 0:
        V_in_points.append(Vo)
    else:
        V_in_points.append(-Vo)
        
    Vpoints.append(V0)
    k1 = h  *f(RC, t , V0, V_in_points[i])
    k2 = h * f(RC, t + 0.5 * h, V0 + 0.5 * k1, V_in_points[i])
    V0 += k2
    i += 1
    
# ----- Parte (d) ----- #

print("# ----- Parte (d) ----- #","\n")
print("En esta parte graficamos el potencial Vin y Vout en función del tiempo.")

subplot(211)
plot(tpoints,V_in_points)
ylabel("Vin (V)")
title("Potenciales en función del tiempo")
subplot(212)
plot(tpoints,Vpoints)
xlabel("Tiempo (s)")
ylabel("Vout (V)")
show()