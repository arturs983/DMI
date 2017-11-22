
# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a	
    print "Izdruka no lietotāj funkcijas a0 = %6.2f S0 = %.2f"%(a,S)


    while k < 3:
    	k = k + 1
   	a = a * (-1) * x**2/((2*k)*(2*k+1))
        a = a * R

   	S = S + a
   	print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

    print "Izdruka no galvenas funkcija Beigas!"
    return S 


x = 1. * input("Izdruka no galvenas funkcijas Lietotāj, lūdzu, ievadi  argumentu (x): ")
y = sin(x)
print "Izdruka no galvenas funkcijas standarta sin(%.2f)=%.2f"%(x,y)
yy = mans_sinuss(x) #funkcijas izpilde un piešķiršana
print "Izdruka no galvenas funkcijas mans sin(%.2f)=%.2f"%(x,yy)
