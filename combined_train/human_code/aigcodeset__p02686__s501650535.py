import sys
sys.setrecursionlimit(1000000000)
import math
from math import gcd

def f1(a1, a2):
    return a1 * a2 // gcd(a1, a2)
from itertools import count, permutations, chain
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint
v1 = lambda: int(input())
v2 = lambda: map(int, input().split())
v3 = lambda: list(v2())
v4 = float('inf')
v5 = 10 ** 9 + 7

def f2(a1, a2, a3):
    while abs(a2 - a3) > 1:
        v1 = (a2 + a3) // 2
        if a1(v1):
            a2 = v1
        else:
            a3 = v1
    return a2

def f3(a1, a2):
    return pow(a1, a2 - 2, a2)

def f4(a1, a2):
    v1 = [1]
    for v2 in range(1, a1 + 1):
        v1.append(v1[-1] * v2 % a2)
    return v1

def f5(a1, a2, a3):
    v1 = [f3(a2[-1], a3)]
    for v2 in range(a1, 1 - 1, -1):
        v1.append(v1[-1] * v2 % a3)
    v1.reverse()
    return v1

def f6(a1, a2, a3):
    v1 = 1
    for v2 in range(a1, a1 - a2, -1):
        v1 = v1 * v2 % a3
    v3 = 1
    for v2 in range(2, a2 + 1):
        v3 = v3 * v2 % a3
    return v1 * f3(v3, a3) % a3

def f7(a1, a2, a3, a4, a5):
    return a4[a1] * a5[a1 - a2] * a5[a2] % a3

class C1:

    def __init__(self, a1):
        self.roots = [-1] * a1

    def getRootID(self, a1):
        v1 = self.roots[a1]
        if v1 < 0:
            return a1
        else:
            v1 = self.getRootID(v1)
            self.roots[a1] = v1
            return v1

    def getGroupSize(self, a1):
        return -self.roots[self.getRootID(a1)]

    def connect(self, a1, a2):
        v1, v2 = (self.getRootID(a1), self.getRootID(a2))
        if v1 == v2:
            return False
        if self.getGroupSize(v1) < self.getGroupSize(v2):
            v1, v2 = (v2, v1)
        self.roots[v1] += self.roots[v2]
        self.roots[v2] = v1
        return True
v6 = 'Yes'
v7 = 'No'

def f11():
    v1 = v1()
    v2 = []
    v3 = []
    for v4 in range(v1):
        v5 = input()
        v6 = 0
        v7 = 0
        for v8 in v5:
            if v8 == '(':
                v6 += 1
            else:
                v6 -= 1
                v7 = min(v7, v6)
        if v6 >= 0:
            v2.append((v6, v7))
        else:
            v3.append((v6, v7))
    v2.sort(key=lambda t: t[1], reverse=True)
    v3.sort(key=lambda t: t[0] - t[1], reverse=True)
    v9 = 0
    for v6, v7 in v2:
        if v9 + v7 >= 0:
            v9 += v6
        else:
            print(v7)
            return
    for v6, v7 in v3:
        if v9 + v7 >= 0:
            v9 += v6
        else:
            print(v7)
            return
    if v9 == 0:
        print(v6)
    else:
        print(v7)
f11()
