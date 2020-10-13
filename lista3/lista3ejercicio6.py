# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:13:28 2020
Autor: Matías López
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def E(q, r0, x, y):
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

nx, ny = 50, 50
x = np.linspace(-1, 1, nx)
y = np.linspace(-1, 1, ny)
X, Y = np.meshgrid(x, y)

dipoles = 1
nq = 2**int(dipoles)
charges = []
for i in range(nq):
    q = i%2 * 2 - 1
    charges.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))

Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges:
    ex, ey = E(*charge, X, Y)
    Ex += ex
    Ey += ey

#Sección del gráfico
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.streamplot(x, y, Ex, Ey, linewidth = 1,
              density = 1.5, arrowstyle='->', arrowsize=1)

charge_colors = {True: 'r', False: 'b'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0]))

ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()