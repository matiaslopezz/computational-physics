# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:16:43 2020
Autor: Matías López
"""
import numpy as np

def errorFunction(x):

#Función que utiliza la regla de Simpson con a = 0, b = x y N = 100.
#Ahora f(x) vale E(x) = e^(-(x^2)); donde: E(0) = 1 y E(b) = e^(-(b^2))
    N = 100
    h = x/N
    s = 1 + np.exp(-x**2)
    
    for k in range(1,N,2): 
        s += 4*np.exp(-(k*h)**2)
        
    for k in range(2,N,2): 
        s += 2*np.exp(-(k*h)**2)   
        
    int = (h/3)*s
    return int

values = []
vector = np.linspace(0,10,100)
    
for i in vector:
    values = np.append(values,errorFunction(i))
        
import matplotlib.pyplot as plt

plt.plot(vector,values, 'b')
plt.title("Error function")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()