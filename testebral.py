def TesteA():
    def F(t,x):
        return 1+(x-t)**2
    x0=-18.95
    t0=1.05
    tf=3
    h=1e-5
    print('a')
    x=Runge_Kutta(x0,t0,tf,h)
    print(x)


def MetEuler(x0,t0,tf,h):

    i=0
    x=x0
    t=t0
    n=(tf-t0)/h
    while i<n:
        t=t+i*h
        x=x+h*F(t,x)
        i+=1
    return x

def Runge_Kutta(x0,t0,tf,h):
    from TesteA import F
    i=0
    x=x0
    t=t0
    n=(tf-t0)/h
    print('c')
    while i<n:
        print('b')
        k1=h*F(t,x)
        k2=h*F(t+0.5*h,x+0.5*k1)
        k3=h*F(t+0.5*h,x+0.5*k2)
        k4=h*F(t+h,x+k3)
        x=x+(k1+2*k2+2*k3+k4)/6
        i+=1
    return x

def main():
    TesteA()
main()