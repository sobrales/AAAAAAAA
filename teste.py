import numpy as np

def Euler(t,tf,x,h):

    while t <= tf:
        x += h*f(t,x)
        t += h
    return x

def Runge_Kutta(t,tf,x,h):

    while t <= tf:
        k1 = h*f(t,x)
        k2 = h*f(t+h/2,x+k1/2)
        k3 = h*f(t+h/2,x+k2/2)
        k4 = h*f(t+h,x+k3)
        x += (k1+2*k2+2*k3+k4)/6
        t += h
    return x

def f(t,x):
    return x

def main():
    t0, tf = 0, 1
    x0 = 1
    h = 1e-5
    e = Euler(t0,tf,x0,h)
    r = Runge_Kutta(t0,tf,x0,h)
    print('Aproximação de Euler',e)
    print(np.e-e)
    print('Aproximação de Runge Kutta',r)
    print(np.e-r)

main()