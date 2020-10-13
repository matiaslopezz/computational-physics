# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:03:45 2020
Autor: Matías López

"""
print("Este programa se basa en calcular la posición de diferentes masas " 
      "acopladas por resortes debido a una fuerza externa sinusoidal aplicada " 
      "en la primera de ellas. Esta posición nos dará información acerca " 
      "de la ampitud de vibración de las masas.","\n")

print("El método a utilizar es el de la eliminaciónn de Gauss.","\n")

print("Las ecuaciones son: ","\n")
print("-m*w^2*x_1 = k(x_2 - x_1) + C --> Primera masa")
print("-m*w^2*x_i = k(x_i+1 - x_i) --> 2 < i < N-1")
print("-m*w^2*x_N = k(x_N-1 - x_N) --> Última masa","\n")

print("Que también se pueden escribir de la siguiente manera:","\n")
print("(a - k)*x_1 - k*x_2 = C")
print("a*x_i - k*x_i-1 - k*x_i+1 = 0")
print("(a - k)*x_N - k*x_N-1 = 0","\n")

from numpy import zeros,empty
from pylab import plot,show,xlabel,ylabel,title

#Constantes
N = 10 #Número de masas
C = 1.0 #Constante de la fuerza sinousoidal: C*exp(iwt)
m = 1.0 #Masa
k = 6.0 #Constante de resorte
w = 2.0 #Frecuencia angular
a = 2*k - m*w*w #Constante alpha definida a partir del sistema de ecuaciones

#Definimos la matriz A -lado izquierdo del sistema- y el array v -lado derecho-
A = zeros([N,N],float)
for i in range(N-1):
    A[i,i] = a
    A[i,i+1] = -k
    A[i+1,i] = -k
    
A[0,0] = a - k
A[N-1,N-1] = a - k
v = zeros(N,float)
v[0] = C

#Eliminación de Gauss
for i in range(N-1):
    
    #Escalerizamos la matriz A
        A[i,i+1] /= A[i,i]
        v[i] /= A[i,i]
        
        A[i+1,i+1] -= A[i+1,i]*A[i,i+1]
        v[i+1] -= A[i+1,i]*v[i]
    
v[N-1] /= A[N-1,N-1]

#Backsubstitution
x= empty(N,float)
x[N-1] = v[N-1]

for i in range(N-2,-1,-1):
    x[i] = v[i] - A[i,i+1]*x[i+1]
    
#Mostramos la solución
print("Las amplitudes son: ")    
print(x)

#Graficamos
plot(x)
plot(x,"ko")
xlabel("Masas")
ylabel("Amplitudes")
title("Amplitudes de masas acopladas por resortes")
show()   