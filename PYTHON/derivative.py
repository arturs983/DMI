
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a	
    while k <500:
        k = k + 1
        R = (-1) * x**2/((2*k)*(2*k+1))
        a = a * R
        S = S + a
    return S 
# funkcijas zimesana
a = 0 #3
b = 3 * np.pi #4
x = np.arange(a,b,0.5) #5
y = mans_sinuss(x) #6a
plt.plot(x,y) #7
plt.grid() #8
#plt.show() #9

# funkcijas atvasinajuma aprekins
n = len(x)
y_prim = []
for i in range(n-1):
    #print i, y[i], y[i+1]
    #print (y[i+1]-y[i])/(x[i+1]-x[i])
    y_prim.append((y[i+1]-y[i])/(x[i+1]-x[i]))
plt.plot(x[:n-1],y_prim)
plt.show()