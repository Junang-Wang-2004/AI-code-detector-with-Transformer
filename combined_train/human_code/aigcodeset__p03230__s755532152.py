import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache

def f1():
    return sys.stdin.readline().strip()

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return list(map(int, f1().split()))

def f5():
    return tuple(map(int, f1().split()))

def f6(a1):
    return zip(*(f3() for v1 in range(a1)))
sys.setrecursionlimit(10 ** 9)
v1 = float('inf')
v2 = 10 ** 9 + 7
from decimal import *
v3 = f2()
v4 = int(0.5 + (2 * v3) ** 0.5)
if v4 * (v4 + 1) == 2 * v3:
    print('Yes')
    print(v4 + 1)
    v5 = [[] for v6 in range(v4 + 1)]
    for v7, (v8, v9) in enumerate(combinations(range(v4 + 1), 2), 1):
        v5[v8].append(v7)
        v5[v9].append(v7)
    for v10 in v5:
        print(v4, *v10)
else:
    print('No')
