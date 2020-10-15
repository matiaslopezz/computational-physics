# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:25:19 2020
Autor: Matías López

"""

#Ejercicio 5

from numpy import array,arange,sqrt
from pylab import plot,xlabel,ylabel,legend,title,show,figure

# ----- Parte (a) ----- #

#Definimos los parámetros
G = 6.6738 * 10 ** -11 * (8760 * 60 * 60) ** 2 #Constante gravitatoria
M = 1.9891 * 10 ** 30 #Masa del Sol en kg

a = 0
b = 3 #En años
h = 1 / 8760 #Un año tiene 8760 horas

x_0 = 1.47 * 10 ** 11
y_0 = 0
vx_0 = 0 
vy_0 = 3.0287 * 10 ** 4 * (8760 * 60 * 60)

def f(r):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    dist = sqrt(x ** 2 + y ** 2)
    return array([vx, - G * M * x /dist ** 3, vy, - G * M * y /dist ** 3],float)

tpoints = arange(a,b,h)
xpoints =[]
ypoints = []
r = array([x_0, vx_0, y_0, vy_0],float)

#Método de Verlet
f_step = 0.5 * h * f(r)
vx_step = r[1] + f_step[1]
vy_step = r[3] + f_step[3]

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[2])
    r[0] += h * vx_step
    r[2] += h * vy_step
    k = h * f(r)
    r[1] = vx_step + 0.5 * k[1]
    r[3] = vy_step + 0.5 * k[3] 
    f_step = 0.5 * h * f(r)
    vx_step += k[1]
    vy_step += k[3]
        
#Gráfico de la trayectoria
figure(1)
plot(xpoints,ypoints)
xlabel("x(m)")
ylabel("y(m)")
title("Trayectoria de la Tierra alrededor del Sol")
show

# ----- Parte (b) ----- #
        
#Definimos los parámetros
G = 6.6738 * 10 ** -11 * (8760 * 60 * 60) ** 2 #Constante gravitatoria
M = 1.9891 * 10 ** 30 #Masa del Sol en kg
m = 5.9722 * 10 ** 24 #Masa de la Tierra en kg

a = 0
b = 3 #En años
h = 1 / 8760 #Un año tiene 8760 horas

x_0 = 1.47 * 10 ** 11
y_0 = 0
vx_0 = 0 
vy_0 = 3.0287 * 10 ** 4 * (8760 * 60 * 60)

def f(r):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    dist = sqrt(x ** 2 + y ** 2)
    return array([vx, - G * M * x /dist ** 3, vy, - G * M * y /dist ** 3],float)

tpoints = arange(a,b,h)
xpoints =[]
ypoints = []
E_potencial = []
E_cinetica = []
r = array([x_0, vx_0, y_0, vy_0],float)

#Método de Verlet
f_step = 0.5 * h * f(r)
vx_step = r[1] + f_step[1]
vy_step = r[3] + f_step[3]

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[2])
    E_potencial.append(- G * M * m / sqrt(r[0] ** 2 + r[2] ** 2))
    E_cinetica.append(0.5 * m * (r[1] ** 2 + r[3] ** 2) )
    r[0] += h * vx_step
    r[2] += h * vy_step
    k = h * f(r)
    r[1] = vx_step + 0.5 * k[1]
    r[3] = vy_step + 0.5 * k[3] 
    f_step = 0.5 * h * f(r)
    vx_step += k[1]
    vy_step += k[3]

#Gráfico de las energías
figure(2)
plot(tpoints, E_potencial, label = "Energía Potencial")
plot(tpoints, E_cinetica, label = "Energía Cinética")
xlabel("Tiempo (años)")
ylabel("Energías (J)")
title("Energía Cinética y Potencial")
legend()
show()

# ----- Parte (c) ------ #
Energia_total = array(E_cinetica, float) + array(E_potencial, float)

figure(3)
plot(tpoints, Energia_total, "k")
xlabel('Tiempo (años)')
ylabel('Energía Total (J)')
title("Energía Total")
show()
    