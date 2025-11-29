import sys, re
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees
from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop, heapify
from functools import reduce

def f1():
    return sys.stdin.readline().strip()

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return list(map(int, f1().split()))

def f5(a1):
    return zip(*(f3() for v1 in range(a1)))
sys.setrecursionlimit(10 ** 9)
v1 = float('inf')
v2 = 10 ** 9 + 7
v3, v4 = f3()
v5 = [f4() for v6 in range(10)]
v7 = [f4() for v6 in range(v3)]
for v8 in range(10):
    for v9 in range(10):
        for v10 in range(10):
            v5[v9][v10] = min(v5[v9][v10], v5[v9][v8] + v5[v8][v10])
v11 = 0
for v9 in range(v3):
    for v12 in v7[v9]:
        if v12 == 1 or v12 == -1:
            continue
        else:
            v11 += v5[v12][1]
print(v11)
