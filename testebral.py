import numpy as np
import math

def MetEuler(x0,t0,tf,h,F):
    i=0
    x=x0
    t=t0
    n=(tf-t0)/h
    while i<=n:
        x=x+h*F(t,x)
        t=t0+i*h
        i+=1
    return x

def Runge_Kutta(x0,t0,tf,h,F):
    i=0
    x=x0
    t=t0
    n=(tf-t0)/h
    #integral=F(t0,x0)*h
    integral=0
    if type(x)!=np.ndarray:
        while i<=n:
            k1=h*F(t,x)
            k2=h*F(t+0.5*h,x+0.5*k1)
            k3=h*F(t+0.5*h,x+0.5*k2)
            k4=h*F(t+h,x+k3)
            x=x+(k1+2*k2+2*k3+k4)/6
            t=t0+i*h
            integral+=F(t,x)*h
            i+=1
    else:
        while i<=n:
            k1=np.dot(F(t,x),h)
            k2=np.dot(F(t+0.5*h,x+np.dot(k1,0.5)),h)
            k3=np.dot(F(t+0.5*h,x+np.dot(k2,0.5)),h)
            k4=np.dot(F(t+h,x+k3),h)
            x=x+np.divide(k1+np.dot(k2,2)+np.dot(k3,2)+k4,6)
            t=t0+i*h
            integral+=np.dot(F(t,x),h)
            i+=1
    return x,integral

def TesteA():   
    def F(t,x):
        return 1+(x-t)**2
    x0=-18.95
    t0=1.05
    tf=3
    h=1e-5
    x,integral=Runge_Kutta(x0,t0,tf,h,F)
    print(integral)
    print(x-x0)

def TesteB():
    A=np.array([[-2,-1,-1,-2],[1,-2,2,-1],[-1,-2,-2,-1],[2,-1,1,-2]])
    def F(t,x):
        return np.dot(A,x)
    x0=np.ones((4,1))
    x0[3]=-1
    t0=0
    tf=2
    h=1e-5
    x,integral=Runge_Kutta(x0,t0,tf,h,F)
    print(integral)
    print(x-x0)

def TesteC():
    n=int(input("Escolha o tamanho da matriz A que deseja"))
    A=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if abs(i-j)==1:
                A[i][j]=1
            elif i==j:
                A[i][j]=-2
    x0=np.zeros(n)
    for i in range(n):
        a=(i+1)/(n+1)
        x0[i]=math.sin(math.pi*a)+math.sin(n*math.pi*a)
    def F(t,x):
        return np.dot(A,X)
        

def main():
    TesteC()
main()