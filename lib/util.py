import math as m
import os
import numpy as np
import matplotlib.pyplot as plt

# CLC 
def clc():
    os.system("cls" if os.name=='nt' else 'clc failed')

# EYE
def eye(n):
    return np.array([ [(1. if y == x else 0.) for y in range(n)] for x in range(n)])

# LINSPACE
def linspace(a: float, b: float, n: int):
    return np.array([ (a + i*(b-a)/(n-1)) for i in range(0, n)])

# LOGSPACE
def logspace(a: float, b: float, n: int):
    # return [ a*(i*(b-a)/(n-1)) for i in range(0, n)]
    return np.logspace(a,b,n)

# ZEROS
def zeros(m, n):
    return np.array([[0. for columns in range(n)] for rows in range(m)])

# ONES
def ones(m, n):
    # return np.array([[1 for columns in range(n)] for rows in range(m)])
    return zeros(m, n) + 1.

# DIAG
def diag(x):
    if(x.ndim == 1): return np.array([ [x[i] if i == j else 0. for i in range(x.shape[0])] for j in range(x.shape[0])])
    else: return np.array([x[i][i] for i in range(x.shape[1])])

# RAND
def rand(m, n):
    return np.array([[np.random.randint(1, 100) for y in range(n)] for x in range(m)])

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()