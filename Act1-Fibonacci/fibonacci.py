"""
Created on Tue Feb 11 07:42:28 2020

@author: Erev14
"""
# import paqueteria
import numpy as np

def traditional(n):
    a, b = 0,1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n):
            a, b = b, a+b
    return a

def nTimeMatrician(n):
    if (n == 0):
        return 0
    f = np.array([[1, 1], [1, 0]])
    m = np.array([[1, 1], [1, 0]])
    for i in range(2, n):
        f = f.dot(m)
    return f[0, 0]

# https://medium.com/@durant.schoon/compute-the-nth-fibonacci-number-in-o-log-n-time-using-python3s-numpy-cc9ae7558323
def logTimeMatrician(n):
    if n == 0:
        return 0
    f = np.array([[1, 1],[1, 0]])
    if n > 1:
        f = power(f, n - 1, m = f)
    return f[0, 0]

def power(f, n, m):
    if n == 1:
        return f
    f = power(f, n // 2, m)
    f = f @ f
    n_even = 2*(n//2)
    if n%2:
        f = f @ m
    return f

# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
f = [0] * 1000
def logTime(n):
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]) :
        return f[n]

    if( n & 1) :
        k = (n + 1) // 2
    else :
        k = n // 2

    # Applyting above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (logTime(k) * logTime(k) + logTime(k-1) * logTime(k-1))
    else :
        f[n] = (2*logTime(k-1) + logTime(k))*logTime(k)

    return f[n]

# https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781782166085/5/ch05lvl1sec93/time-for-action-computing-fibonacci-numbers
def formula1Time(n):
    n = np.arange(1, n+1)
    if n.shape == (0,):
        return 0
    sqrt5 = np.sqrt(5)
    phi = (1 + sqrt5)/2
    f_inverted = np.rint( ( phi**n - (-1/phi)**n)/sqrt5)
    return int(f_inverted[-1])

if __name__ == "__main__":
    for i in range(0,10):
        print("iteracion" + str(i))
        print(formula1Time(i))
