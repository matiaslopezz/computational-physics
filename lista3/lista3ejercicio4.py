# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:47:55 2020
Autor: Matías López
"""
from scipy.integrate import quadrature
import numpy as np

# ----- Parte (a) ----- #
def harmonicOscillatorPeriod(a,k,m):
    def potential(x):
        return 0.5*k*x**2
    
    integral,g = quadrature(lambda x: 1/(np.sqrt(potential(a) - potential(x))), 0, a)
    return integral*(np.sqrt(8*m))

# ----- Parte (b) ----- #
def harmonicOscillatorPeriod_2(a,m):
    def potential(x):
        return x**4
    
    integral,g = quadrature(lambda x: 1/(np.sqrt(potential(a) - potential(x))), 0, a)
    return integral*(np.sqrt(8*m))
