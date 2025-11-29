import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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
sys.setrecursionlimit(10 ** 9)
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = f2()
v4 = list(f1())
v5 = f2()

class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 1)

    def sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.tree[a1]
            a1 -= a1 & -a1
        return v1

    def add(self, a1, a2):
        while a1 <= self.size:
            self.tree[a1] += a2
            a1 += a1 & -a1
v6 = defaultdict(int)
for v7, v8 in enumerate(ascii_lowercase):
    v6[v8] = v7
v9 = [None] * len(ascii_uppercase)
for v7 in range(len(ascii_uppercase)):
    v9[v7] = C1(v3)
for v7 in range(v3):
    v9[v6[v4[v7]]].add(v7 + 1, 1)
for v10 in range(v5):
    v11, v12, v13 = f1().split()
    if v11 == '1':
        v12 = int(v12)
        v8 = v4[v12 - 1]
        v9[v6[v8]].add(v12, -1)
        v9[v6[v13]].add(v12, 1)
        v4[v12 - 1] = v13
    if v11 == '2':
        v14 = 0
        v12, v13 = (int(v12), int(v13))
        for v7 in range(len(ascii_uppercase)):
            v14 += v9[v7].sum(v13) - v9[v7].sum(v12 - 1) >= 1
        print(v14)
