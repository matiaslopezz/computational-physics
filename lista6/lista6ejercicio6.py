# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:53:19 2020
Autor: Matías López

"""
#Ejercicio 6

from numpy import arange,array,zeros,radians
from pylab import plot,xlabel,ylabel,legend,figure,title
from math import sin,pi

# ----- Parte (a) ----- #

#La ecuación diferencial a resolver es: dw/dt = -(g/l)/sin(theta)
#Usaremos el método de Runge-Kuta.

l = 1 #largo del hilo -en metros-
g = 9.81 #aceleración gravitatoria -en ms**-2-

#Condiciones iniciales
thetas_0 = [0,45,90,180]
omegas_0 = [0]*len(thetas_0)

a = 0 
b = 12
N = 12000
h = (b - a)/N
tpoints = arange(a,b,h)

def f(r,t): 
    theta = r0[0]
    omega = r0[1]
    
    ftheta = omega
    fomega = - (g/l) * sin(theta)
    
    return array([ftheta, fomega], float)

for i in range(len(thetas_0)):
    #Condición inicial
    theta_0 = radians(thetas_0[i])
    omega_0 = omegas_0[i]
    
    r0 = [theta_0,omega_0]

    thetapoints = zeros(N)
    omegapoints = zeros(N)

    for t in range(len(tpoints)-1):
        thetapoints[0] = r0[0]
        omegapoints[0] = r0[1]
    
        k1 = h * f(r0,tpoints[t])
        k2 = h * f(r0 + 0.5 * k1, tpoints[t] * 0.5 * h) 
   
        thetapoints[t+1] = thetapoints[t] + k2[0]
        omegapoints[t+1] = omegapoints[t] + k2[1]
        r0 = [thetapoints[t],omegapoints[t]]
    
    figure(1)
    plot(tpoints,thetapoints,label = thetas_0[i])
    xlabel("Tiempo (s)")
    ylabel("Amplitud (rad)")
    legend()
    title("Amplitud del péndulo no lineal dadas varias C.I.")
    
# ----- Parte (b) ----- #

g = 9.81
l = 0.1
theta_0 = 63 * pi / 180
omega_0 = 0.0
t_inicial = 0.0
t_final = 10.0
N = 5000
h = (t_final - t_inicial) / N

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = - (g / l) * sin(theta)
    return array([ftheta, fomega], float)

tpoints = arange(t_inicial, t_final, h)
thetapoints = []
r = array([theta_0, omega_0], float)

for t in tpoints:
    thetapoints.append(r[0])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plot theta vs t
figure(2)
plot(tpoints, (array(thetapoints,float) * 180 / pi))
xlabel("Tiempo (s)")
ylabel("Theta (grados)")