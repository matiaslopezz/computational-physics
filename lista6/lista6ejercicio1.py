# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:17:49 2020
Autor: Matías López

"""
#Ejercicio 1 - La Caída de la Pelota

#Modelo 1D de una esfera cayendo
from numpy import sqrt,tanh,cosh,log,linspace,arange,append
from pylab import plot,subplot,xlabel,ylabel,title

def velocity(m, A, g, rho, D, t):
    vy = sqrt((2*m*g)/(D*rho*A))*tanh(sqrt((D*rho*A*g)/(2*m))*t)
    return vy
    
def position(m, A, g, rho, D, t):
    y = ((2*m)/(D*rho*A))*log(cosh(sqrt((D*rho*A*g)/(2*m))*t))
    return y

#Constantes
m =  0.058  #Masa de la pelota -de tenis-
A = 0.065 #Área frontal de la pelota
g = 9.8 #Aceleración gravitatoria
rho = 1.225 #Densidad del aire
D = 0.5 #Coeficiente de arrastre

t = linspace(0,100,100)
velocity(0.058,0.013,9.8,1.225,0.5,t)
position(0.058,0.013,9.8,1.225,0.5,t)
ti = 0
tf = 30
dt = 0.1
y0 = 158
v0 = 0

tpoints = arange(ti,tf+dt,dt)
ypoints = []
vpoints = []

for t in tpoints:
    ypoints = append(ypoints,y0)
    vpoints = append(vpoints,v0)
    y0 -= v0*dt
    v0 += (g-((D*rho*A)/(2*m))*v0**2)*dt

subplot(211)
plot(tpoints,ypoints)
title("Pelota de tenis en caída")
ylabel("Altura (m)")
subplot(212)
plot(tpoints,vpoints)
xlabel("Tiempo (s)")
ylabel("Velocidad (m/s)")
