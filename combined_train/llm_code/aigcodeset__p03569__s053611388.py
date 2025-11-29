import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd

def f1():
    return sys.stdin.readline().strip()

def f2():
    return f1()

def f3():
    return int(f1())

def f4():
    return float(f1())

def f5():
    return map(int, f1().split())

def f6():
    return map(str, f1().split())

def f7():
    return list(map(int, f1().split()))

def f8():
    return list(map(str, f1().split()))

def f9(a1, a2):
    return a1 * a2 // gcd(a1, a2)
sys.setrecursionlimit(10 ** 9)
v1 = sys.maxsize
v2 = 10 ** 9 + 7
v3 = [0, 0, 1, -1, 1, -1, -1, 1]
v4 = [1, -1, 0, 0, 1, -1, 1, -1]
v5 = f2()
v6 = len(v5)
v7 = 0
v8 = v6 - 1
v9 = True
while v7 < v8:
    if v5[v7] != v5[v8]:
        v9 = False
        break
    v7 += 1
    v8 -= 1
if v9:
    print(0)
    exit()
v10 = []
for v7 in range(v6):
    if v5[v7] != 'x':
        v10.append(v5[v7])
v11 = len(v10)
v7 = 0
v8 = v11 - 1
v9 = True
while v7 < v8:
    if v10[v7] != v10[v8]:
        v9 = False
        break
    v7 += 1
    v8 -= 1
if not v9:
    print(-1)
    exit()
v12 = 0
v8 = 0
for v7 in range(v6):
    if v5[v7] == 'x':
        continue
    if v8 == v11 // 2:
        v12 = v7
        break
    v8 += 1
v7 = 0
v8 = v6 - 1
v13 = 0
while v7 < v12:
    if v5[v7] == 'x' and v5[v8] == 'x' or (v5[v7] != 'x' and v5[v8] != 'x'):
        v7 += 1
        v8 -= 1
    elif v5[v7] == 'x':
        v7 += 1
        v13 += 1
    elif v5[v8] == 'x':
        v8 -= 1
        v13 += 1
if v11 % 2 == 0:
    v12 -= 1
v13 += v12 - v7
print(v13)
