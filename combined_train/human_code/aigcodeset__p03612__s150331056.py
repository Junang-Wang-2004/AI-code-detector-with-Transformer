import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from heapq import heappop, heapify, heappush

def f1():
    return sys.stdin.readline().strip()

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return map(str, f1().split())

def f5():
    return list(map(int, f1().split()))

def f6():
    return list(map(str, f1().split()))
sys.setrecursionlimit(10 ** 9)
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = f2()
v4 = f5()
v5 = 0
v6 = 0
while v6 < v3:
    if v4[v6] == v6 + 1:
        v5 += 1
        v6 += 1
    v6 += 1
print(v5)
