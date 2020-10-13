# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:51:45 2020
Autor: Matías López
"""
# ----- Parte (a) ----- #
import numpy as np
from scipy.integrate import quadrature

def debyeIntegrand(x): 
    return (x**4*np.exp(x))/(np.exp(x)-1)**2

def heatCapacity(debyeIntegrand, T, V, rho, T_D):
    debyeIntegrand,w = quadrature(debyeIntegrand, 0, T_D/T)
    k = 1.380648813e-23
    c_v = 9*V*rho*k*(T/T_D)**3*debyeIntegrand
    return c_v    

c = heatCapacity(debyeIntegrand,1,0.001,6.022e28,428)
print("Calor específico del aluminio -adimensionado-: ", c)
#Aluminium:
    #density -> rho = 6.022e28 m**-3
    #volume -> V = 1000 cm**3
    
# ----- Parte (b) ----- #
values = []
temperatures = np.linspace(5,500,100)

for j in temperatures:
    values = np.append(values,heatCapacity(debyeIntegrand,j,0.001,6.022e28,428))
    
import matplotlib.pyplot as plt

plt.plot(temperatures, values, "r")
plt.title("Debye Model")
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity")
plt.show()
