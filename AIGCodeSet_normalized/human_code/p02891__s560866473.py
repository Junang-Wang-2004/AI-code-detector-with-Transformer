import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
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
v3 = f1()
v4 = f2()
v5 = []
v6 = 1
for v7 in range(1, len(v3)):
    if v3[v7] == v3[v7 - 1]:
        v6 += 1
    else:
        v5.append(v6)
        v6 = 1
v5.append(v6)
if v3[0] != v3[-1]:
    print(sum([x // 2 for v8 in v5]) * v4)
elif len(v5) == 1:
    print(len(v3) * v4 // 2)
else:
    v9 = v5[1:-1] + [v5[0] + v5[-1]]
    print(sum([v8 // 2 for v8 in v9]) * (v4 - 1) + sum([v8 // 2 for v8 in v5]))
