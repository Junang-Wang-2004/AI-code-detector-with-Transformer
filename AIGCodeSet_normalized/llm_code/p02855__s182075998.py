from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)

def f1():
    return sys.stdin.readline().strip()

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return list(f3())
v1, v2, v3 = f3()
v4 = []
v5 = []
v6 = []
for v7 in range(v1):
    v4.append(f1())
    if v4[v7].count('#') > 0:
        v5.append(v7)
    else:
        v6.append(v7)
v8 = [[0] * v2 for v7 in range(v1)]
v9 = 0
for v7 in v5:
    v9 += 1
    v3 = 0
    while v4[v7][v3] == '.':
        v8[v7][v3] = v9
        v3 += 1
    v8[v7][v3] = v9
    v3 += 1
    if v3 < v2:
        for v10 in range(v3, v2):
            if v4[v7][v10] == '#':
                v9 += 1
            v8[v7][v10] = v9
for v7 in v6:
    v3 = v7 - 1
    while v3 >= 0 and v8[v3][0] == 0:
        v3 -= 1
    if v3 < 0:
        v3 = v7 + 1
        while v3 < v1 and v8[v3][0] == 0:
            v3 += 1
    for v10 in range(v2):
        v8[v7][v10] = v8[v3][v10]
for v7 in range(v1):
    print(*v8[v7][:])
