import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

def f1():
    return sys.stdin.readline()[:-1]

def f2(a1):
    return [0] + list(accumulate(a1))
sys.setrecursionlimit(500000)
v1 = pow(10, 9) + 7
v2 = [chr(ord('a') + i) for v3 in range(26)]
v4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
v5 = int(f1())
v6 = [int(f1()) for v3 in range(v5)]
v6.sort()
v7 = 0
if v5 % 2 == 0:
    for v3 in range(v5):
        if v3 < v5 // 2:
            v7 -= v6[v3] * 2
        else:
            v7 += v6[v3] * 2
    v7 -= v6[v5 // 2]
    v7 += v6[v5 // 2 - 1]
    print(v7)
else:
    for v3 in range(v5):
        if v3 < v5 // 2:
            v7 -= v6[v3] * 2
        elif v3 > v5 // 2:
            v7 += v6[v3] * 2
    print(max(v7 + v6[v5 // 2] - v6[v5 // 2 + 1], v7 - v6[v5 // 2] + v6[v5 // 2 - 1]))
