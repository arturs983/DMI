from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    a1 = (-1)**1*x**1/6
    S1 = a1 + a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
    print "a%d = %6.2f S%d = %6.2f"%(k+1,a1,k+1,S1)
    arra=[]
    arrS=[]

    while k < 500:
        k = k + 1
        R = (-1) * x**2/((2*k)*(2*k+1))
        a = a * R
        S=S+a
        #print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
        arra.append(a)
        arrS.append(S)

    print "a%d = %6.2f S%d = %6.2f"%(k-1,arra[-2],k-1,arrS[-2])
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
    #print "Beigas!"
    return S

x=1. * input("Lietotaj, ludzu, ievadi x argumentu: ")
y=sin(x)
print "Standarta sin(%.2f) = %.2f"%(x,y)
yy = mans_sinuss(x)
print "Mans sin(%.2f) = %.2f"%(x,yy)

