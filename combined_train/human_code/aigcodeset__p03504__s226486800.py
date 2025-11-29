import sys
from collections import *
import heapq
import math
import bisect
import copy
from itertools import permutations, accumulate, combinations, product

def f1():
    return sys.stdin.readline()[:-1]

def f2(a1):
    return [0] + list(accumulate(a1))
v1 = pow(10, 9) + 7
v2 = [chr(ord('a') + i) for v3 in range(26)]
v4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
v5, v6 = map(int, f1().split())
v7 = [list(map(int, f1().split())) for v3 in range(v5)]
v7.sort()
v8 = [0] * v6
for v3 in range(v5):
    v9, v10, v11 = v7[v3]
    for v12 in range(v6):
        if v8[v12] == 0:
            v8[v12] = v7[v3]
            break
        elif v8[v12][2] == v11:
            v8[v12] = v7[v3]
            break
        elif v8[v12][1] < v9:
            v8[v12] = v7[v3]
            break
v13 = 0
for v3 in range(v6):
    if v8[v3] != 0:
        v13 += 1
print(v13)
