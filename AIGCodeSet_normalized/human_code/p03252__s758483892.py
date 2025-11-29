import math
import copy
import sys
import fractions
import numpy as np
from functools import reduce

def f1():
    v1 = int(input())
    return v1

def f2():
    v1 = []
    v2 = input().split()
    v3 = [int(n) for v4 in v2]
    return v3

def f3(a1):
    v1 = []
    for v2 in range(a1):
        v3 = int(input())
        v1.append(v3)
    return v1

def f4(a1):
    v1 = []
    v2 = []
    for v3 in range(a1):
        v4 = input().split()
        v1 = [int(a1) for a1 in v4]
        v2.append(v1)
    return v2

def f5():
    v1 = str(input())
    return v1
v1 = f5()
v2 = f5()
v3 = []
v3 = list(v1)
v4 = []
v4 = list(v2)
v5 = len(v3)
v6 = {}
v7 = {}
v8 = True
for v9 in range(v5):
    v10 = v3[v9]
    v11 = v4[v9]
    if v10 not in v6:
        v6[v10] = v11
    elif v6[v10] != v11:
        v8 = False
        break
    if v11 not in v7:
        v7[v11] = v10
    elif v7[v11] != v10:
        v8 = False
        break
if v8:
    print('Yes')
else:
    print('No')
