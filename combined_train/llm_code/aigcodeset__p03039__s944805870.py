import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
from math import gcd

def f1():
    return sys.stdin.readline()[:-1]

def f2(a1):
    return [0] + list(accumulate(a1))
v1 = pow(10, 9) + 7
v2 = [chr(ord('a') + i) for v3 in range(26)]
v4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
v5, v6, v7 = map(int, f1().split())

def f3(a1, a2, a3=10 ** 9 + 7):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return g1[a1] * g2[a2] * g2[a1 - a2] % a3
v8 = 2 * 10 ** 5 + 10
v9 = [1, 1]
v10 = [1, 1]
v11 = [0, 1]
for v3 in range(2, v8 + 1):
    v9.append(v9[-1] * v3 % v1)
    v11.append(-v11[v1 % v3] * (v1 // v3) % v1)
    v10.append(v10[-1] * v11[-1] % v1)
v12 = 0
for v3 in range(v5):
    v12 += v3 * (v5 - v3) * v6 * v6 * f3(v5 * v6 - 2, v7 - 2)
    v12 %= v1
for v3 in range(v5):
    v12 += v3 * (v5 - v3) * v6 * v6 * f3(v5 * v6 - 2, v7 - 2)
    v12 %= v1
print(v12)
