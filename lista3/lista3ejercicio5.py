# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:07:57 2020
Autor: Matías López
"""

import numpy as np
from pylab import plot,xlabel,title,show

def f(x):
    return 1 + 0.5*np.tanh(2*x)

h = 0.5
x = np.linspace(-2, 2)

central_derivate = (f(x + 0.5*h) - f(x - 0.5*h))/h
analitic_derivate = 1/np.cosh(2*x)**2

plot(x,central_derivate,"o")
plot(x,analitic_derivate,"")
title("sech(x)")
xlabel("x")
show()
