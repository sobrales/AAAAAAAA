import numpy as np

'''def Euler(t,tf,x,h):

    while t <= tf:
        x += h*f(t,x)
        t += h
    return x'''

def Runge_Kutta(t,tf,x,h):

    while t <= tf:
        '''k1 = h*f(t,x)
        k2 = h*f(t+h/2,x+k1/2)
        k3 = h*f(t+h/2,x+k2/2)
        k4 = h*f(t+h,x+k3)
        x += (k1+2*k2+2*k3+k4)/6'''
        k1 = np.multiply(h,f(t,x))
        k2 = np.multiply(h,f(t+h/2,x+k1/2))
        k3 = np.multiply(h,f(t+h/2,x+k2/2))
        k4 = np.multiply(h,f(t+h,x+k3))
        x = np.add(x,np.divide(np.add(np.add(k1,np.multiply(2,k2)),np.add(np.multiply(2,k3),k4)),6))
        t += h
    return x

def f(t,x): # x' = x
    '''return x

def f_teste1(t,x):'''
    return 1 + (x-t)**2

def f_teste2(t,x):
    A = np.array([[-2,-1,-1,-2],[1,-2,2,-1],[-1,-2,-2,-1],[2,-1,1,-2]])
    return np.matmul(A,x)


def main():
    h = 1e-5
<<<<<<< HEAD
    escolha = '1'
    if escolha == '1':
        t0, tf = 1.05, 3
        x0 = -18.95
    elif escolha == '2':
        t0, tf = 0, 2
        x0 = np.array([1,1,1,-1])
    '''euler = Euler(t0,tf,x0,h)
    print('Aproximação de Euler',euler)'''
    kutta = Runge_Kutta(t0,tf,x0,h)
    print('Aproximação de Runge Kutta',kutta)

=======
    e = Euler(t0,tf,x0,h)
    r = Runge_Kutta(t0,tf,x0,h)
    print('Aproximação de Euler',e)
    print(np.e-e)
    print('Aproximação de Runge Kutta',r)
    print(np.e-r)
>>>>>>> 6549e04ea7262947e1942749f7cc773ba91ff530
main()