import numpy as np

'''def Euler(t,tf,x,h):

    while t <= tf:
        x += h*f(t,x)
        t += h
    return x'''

def Runge_Kutta(t,tf,x,h,teste):
    #soma = 0#np.multiply(h,f(t,x,teste))

    while t <= tf:
        '''k1 = h*f(t,x)
        k2 = h*f(t+h/2,x+k1/2)
        k3 = h*f(t+h/2,x+k2/2)
        k4 = h*f(t+h,x+k3)
        x += (k1+2*k2+2*k3+k4)/6'''
        k1 = np.multiply(h,f(t,x,teste))
        k2 = np.multiply(h,f(t+h/2,x+k1/2,teste))
        k3 = np.multiply(h,f(t+h/2,x+k2/2,teste))
        k4 = np.multiply(h,f(t+h,x+k3,teste))
        x = np.add(x,np.divide(np.add(np.add(k1,np.multiply(2,k2)),np.add(np.multiply(2,k3),k4)),6))
        #soma += np.multiply(h,f(t,x,teste))
        t += h
    return x#, soma

def f(t,x,teste):
    if teste == '1':
        return 1 + (x-t)**2
    elif teste == '2':
        A = np.array([[-2,-1,-1,-2],[1,-2,2,-1],[-1,-2,-2,-1],[2,-1,1,-2]])
        return np.matmul(A,x)


def main():
    h = 1e-5
    teste = input('escolhe aí fera: ')
    if teste == '1':
        t0, tf = 1.05, 3
        x0 = -18.95
    elif teste == '2':
        t0, tf = 0, 2
        x0 = np.array([[1],[1],[1],[-1]])
    elif teste == '3':
        n = input('n: ')
        x0 = np.zeros(n)
        for i in range(n):
            x0[i] = np.sin(np.pi*(i/(n+1))) + np.sin(n*np.pi*(i/(n+1)))



    '''euler = Euler(t0,tf,x0,h)
    print('Aproximação de Euler',euler)'''
    x = Runge_Kutta(t0,tf,x0,h,teste)
    print('x:',x)
    print('integral:',np.subtract(x,x0))

main()