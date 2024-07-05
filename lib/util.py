import math as m
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle as p

### CLASSES:
class MATStruct:
    def __init__(self, d: dict) -> None:
        for entry in d.keys():
            setattr(self, entry, d[entry])

    def __add__(self, other):
        for other_names in vars(other).keys():
            setattr(self, other_names, vars(other)[other_names])
        return self

    def delete(self, name: str) -> None:
        if name in dir(self): del vars(self)[name]
        else: print("No variable with the name " + name + " was found!")

    def add(self, name: str, obj) -> None:
        setattr(self, name, obj)


colors1 = {
    "blue" : 5,
    "red" : 6,
    "yellow" : 7,
    }

colors2 = {
    "green" : 8,
    "purple" : 9,
    "black" : 10,
    }

a = MATStruct(colors1)
b = MATStruct(colors2)
# print(vars(a+b))
# print(vars(b))

### FUNCTIONS:
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

# MAKE FILE TO STORE VARIABLES
def create_file(filename: str):
    open(filename, 'x') # only creates the file
    print("File Created Successfully!")

# WRITE GLOBALS TO FILE
def write(filename: str, overwrite=False, vars=[]) -> None:
    with open(filename, 'ab' if not overwrite else 'wb') as file:
        d = {}
        if vars == []:
            for name, val in myvars().items(): d.update({name: val})
        else:
            for name, val in vars: d.update({name: val})
        p.dump(d, file)


# READ FROM FILE
def load(filename: str):
    with open(filename, "rb") as file:
        return MATStruct(p.load(file))

def myvars() -> dict[str, any]:
    # return {name: val for name, val in globals().items() if type(val) != type(print()) or type(val) != type(m)}
    d = {}
    for name, val in globals().items():
        if type(val) != type(print) and type(val) != type(m) and type(val) != type(myvars) and not name.startswith("__"):
            d.update({name: val})
    return d

def whos(filename: str=""):
    

### ----------------------------------------------------------------------------------###

def pfd(n: int) -> list[int]:
    ret = []
    i = n
    while i % 2 == 0:
        i /= 2
        ret.append(2)

    return ret + [i for i in range(2, int(m.sqrt(n) + 1), 2) if n % i == 0]

    for i in range(3, int(m.sqrt(n)), 2):
        while n % i == 0:
            n /= i
            ret.append(i)
                 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxs = []
        for i in range(len(nums)):
            temp = []
            for j in range(i, len(nums)):
                temp.append(nums[j])
                maxs.append(sum(temp))
        return max(maxs)

    def findMaximumXOR(self, nums: list[int]) -> int:
        return max([nums[j] ^ nums[i] for i in range(len(nums)) for j in range(i, len(nums))])
    
    