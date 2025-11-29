import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
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
from decimal import *
v3 = 10 ** 5
v4 = [1] * (v3 + 1)
for v5 in range(1, v3 + 1):
    v4[v5] = v5 * v4[v5 - 1] % v2
v6 = [1] * (v3 + 1)
v6[v3] = pow(v4[v3], v2 - 2, v2)
for v5 in range(v3, 0, -1):
    v6[v5 - 1] = v5 * v6[v5] % v2

def f6(a1, a2):
    if a1 < a2:
        return 0
    else:
        return v4[a1] * v6[a2] % v2 * v6[a1 - a2] % v2
v7, v8 = f3()
v9 = f4()
v9.sort()
v10 = 0
for v11 in range(v8 - 1, v7):
    v10 = (v10 + v9[v11] * f6(v11, v8 - 1) % v2) % v2
v9 = v9[::-1]
v12 = 0
for v11 in range(v8 - 1, v7):
    v12 = (v12 + v9[v11] * f6(v11, v8 - 1) % v2) % v2
print((v10 - v12) % v2)
