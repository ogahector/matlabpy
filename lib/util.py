import math as m
import os
import numpy as np
import matplotlib as plot

# CLC 
def clc():
    os.system("cls" if os.name=='nt' else 'clc failed')

# EYE
def eye(n):
    return [ [(1. if y == x else 0.) for y in range(n)] for x in range(n)]

# LINSPACE
def linspace(a: float, b: float, n: int):
    return [ (a + i*(b-a)/n) for i in range(0, n+1)]

print(linspace(1, 10, 10))
print(np.linspace(1, 10, 10))