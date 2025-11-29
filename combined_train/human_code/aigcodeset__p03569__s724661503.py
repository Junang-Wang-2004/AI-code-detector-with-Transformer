import sys
import heapq
import re
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from math import factorial, sqrt, ceil, gcd
from functools import lru_cache, reduce
from decimal import Decimal
from operator import mul
v1 = 1 << 60
v2 = 1000000007
sys.setrecursionlimit(10 ** 7)

class C1:

    def __init__(self, a1):
        self.n = a1
        self.parents = [-1] * a1

    def find(self, a1):
        if self.parents[a1] < 0:
            return a1
        else:
            self.parents[a1] = self.find(self.parents[a1])
            return self.parents[a1]

    def union(self, a1, a2):
        a1 = self.find(a1)
        a2 = self.find(a2)
        if a1 == a2:
            return
        if self.parents[a1] > self.parents[a2]:
            a1, a2 = (a2, a1)
        self.parents[a1] += self.parents[a2]
        self.parents[a2] = a1

    def size(self, a1):
        return -self.parents[self.find(a1)]

    def same(self, a1, a2):
        return self.find(a1) == self.find(a2)

    def members(self, a1):
        v1 = self.find(a1)
        return [i for v2 in range(self.n) if self.find(v2) == v1]

    def roots(self):
        return [i for v1, v2 in enumerate(self.parents) if v2 < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for v1 in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for v1 in self.roots()))

def f9(a1, a2, a3):
    v1 = [10 ** 20] * a3
    v2 = [True] * a3
    v1[a1] = 0
    v2[a1] = False
    v3 = []
    for v4, v5 in a2[a1]:
        heapq.heappush(v3, v4 * 10 ** 6 + v5)
    while len(v3):
        v6 = heapq.heappop(v3)
        if not v2[v6 % 10 ** 6]:
            continue
        v7 = v6 % 10 ** 6
        v1[v7] = v6 // 10 ** 6
        v2[v7] = False
        for v8 in a2[v7]:
            if v2[v8[1]]:
                heapq.heappush(v3, (v8[0] + v1[v7]) * 10 ** 6 + v8[1])
    return v1

def f10(a1):
    v1 = []
    v2 = a1
    for v3 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v2 % v3 == 0:
            v4 = 0
            while v2 % v3 == 0:
                v4 += 1
                v2 //= v3
            v1.append([v3, v4])
    if v2 != 1:
        v1.append([v2, 1])
    if v1 == []:
        v1.append([a1, 1])
    return v1

def f11(a1, a2):
    if a1 < a2:
        return 0
    a2 = min(a2, a1 - a2)
    v2 = reduce(mul, range(a1, a1 - a2, -1), 1)
    v3 = reduce(mul, range(1, a2 + 1), 1)
    return v2 // v3

def f12(a1, a2):
    return a1 * a2 // gcd(a1, a2)

def f13(a1):
    return reduce(f12, a1, 1)

def f14(a1):
    return reduce(gcd, a1)

def f15(a1):
    if a1 <= 1:
        return False
    v1 = 2
    while True:
        if v1 ** 2 > a1:
            break
        if a1 % v1 == 0:
            return False
        v1 += 1
    return True

def f16(a1):
    v1 = [i for v2 in range(2, a1 + 1)]
    v3 = []
    while True:
        v4 = min(v1)
        if v4 > sqrt(a1):
            break
        v3.append(v4)
        v2 = 0
        while v2 < len(v1):
            if v1[v2] % v4 == 0:
                v1.pop(v2)
                continue
            v2 += 1
    for v5 in v1:
        v3.append(v5)
    return v3

def f17(a1):
    if a1 == []:
        return [[]]
    else:
        v1 = []
        v2 = sorted(set(a1))
        for v3 in v2:
            v4 = a1[:]
            v4.remove(v3)
            for v5 in f17(v4):
                v1.append([v3] + v5)
        return v1

def f18(a1):
    v1, v2 = ([], [])
    v3 = 1
    while v3 * v3 <= a1:
        if a1 % v3 == 0:
            v1.append(v3)
            if v3 != a1 // v3:
                v2.append(a1 // v3)
        v3 += 1
    return v1 + v2[::-1]
v3 = input()
v4 = len(v3)

def f19(a1, a2):
    if 'x' not in a1:
        if a1 == a1[::-1]:
            return 0
        else:
            return -1
    else:
        v1 = a1.replace('x', '')
        if v1 != v1[::-1]:
            return -1
        v2 = 0
        v3 = a1
        v4 = 0
        while True:
            v5 = len(v3)
            if v4 >= v5:
                break
            if v3[v4] == 'x' and v3[v5 - v4 - 1] != 'x':
                v3 = v3[:v4] + v3[v4 + 1:]
                v2 += 1
            elif v3[v4] != 'x' and v3[v5 - v4 - 1] == 'x':
                v3 = v3[:v5 - v4 - 1] + v3[v5 - v4:]
                v2 += 1
            else:
                v4 += 1
        return v2
v5 = f19(v3, v4)
print(v5)
