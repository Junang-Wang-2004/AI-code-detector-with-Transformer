import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd

def f1(*a1):
    if debugmode:
        print(*a1)

def f2():
    return sys.stdin.readline().strip()

def f3():
    return f2()

def f4():
    return int(f2())

def f5():
    return float(f2())

def f6():
    return map(int, f2().split())

def f7():
    return map(str, f2().split())

def f8():
    return list(map(int, f2().split()))

def f9():
    return list(map(str, f2().split()))

def f10(a1, a2):
    return a1 * a2 // gcd(a1, a2)
sys.setrecursionlimit(10 ** 9)
v1 = sys.maxsize
v2 = 10 ** 9 + 7
v3 = [0, 0, 1, -1, 1, -1, -1, 1]
v4 = [1, -1, 0, 0, 1, -1, 1, -1]
v5 = False
v6 = list(f3())
v7 = True
if v6.count('N') and (not v6.count('S')):
    v7 = False
if v6.count('E') and (not v6.count('W')):
    v7 = False
if not v6.count('N') and v6.count('S'):
    v7 = False
if not v6.count('E') and v6.count('W'):
    v7 = False
if v7:
    print('Yes')
else:
    print('No')
