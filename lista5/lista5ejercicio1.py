# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:14:53 2020
Autor: Matías López

"""

import pandas as pd
from numpy import array,empty,loadtxt,linalg,copy

mat = array([[0,-1,0],
             [2,6,-5],
             [1,1,-1]],float)

df = pd.DataFrame(mat.astype(int))
df.to_csv('matrix.txt',sep=',',header=False, float_format='%.2f', index=False)

#Matriz que multiplica las variables del sistema
m = loadtxt('matrix.txt',delimiter=',')

#Vector a la derecha que verifica la igualdad de la ecuación
v = array([1,-4,3],float)
N = len(v)

if (linalg.det(m))==0:
     print("Error, m es una matriz singular")

#Gauss elimination
for i in range(N):
    
    #Pivoteo parcial
    
    largest = abs(m[i, i])
    largest_row = i
    
    for a in range(i + 1, N):
        if abs(m[a, i]) > largest:
            largest = abs(m[a, i])
            largest_row = a
            
    if largest_row != i:
        
        #Cambio filas en la matriz m
        current_row = copy(m[i, :])
        m[i, :] = m[largest_row, :]
        m[largest_row, :] = current_row

        #Cambio filas en la matriz v
        v[i], v[largest_row] = v[largest_row], v[i]
    
    #Fin del pivoteo parcial
    
    #Escalerizamos la matriz m
    div = m[i,i]
    m[i,:] /= div
    v[i] /= div
    
    for j in range(i+1,N):
        mult = m[j,i]
        m[j,:] -= mult*m[i,:]
        v[j] -= mult*v[i]

#Backsubstitution
x = empty(N,float)

for k in range(N-1,-1,-1):
    x[k] = v[k]
    
    for l in range(k+1,N):
        x[k] -= m[k,l]*x[l]
        
print("x = ",x)



