import math
import fractions
import bisect
import collections
import itertools
import heapq
import string
import sys
import copy
from decimal import *
from collections import deque
from math import gcd
sys.setrecursionlimit(10 ** 7)
v1 = 10 ** 9 + 7
v2 = float('inf')

def f1(a1, a2):
    return a1 * a2 // gcd(a1, a2)

def f2():
    return int(sys.stdin.readline())

def f3():
    return float(sys.stdin.readline())

def f4():
    return sys.stdin.readline().split()

def f5():
    return map(int, sys.stdin.readline().split())

def f6():
    return map(lambda x: int(x) - 1, sys.stdin.readline().split())

def f7():
    return map(float, sys.stdin.readline().split())

def f8():
    return list(map(int, sys.stdin.readline().split()))

def f9():
    return sorted(f8())

def f10():
    return sorted(f8(), reverse=True)

def f11():
    return list(map(float, sys.stdin.readline().split()))

def f12(a1, a2=''):
    return a2.join(a1)

def f13(a1, a2):
    return itertools.permutations(a1, a2)

def f14(a1, a2):
    return math.factorial(a1) // math.factorial(a1 - a2)

def f15(a1, a2):
    return itertools.combinations(a1, a2)

def f16(a1, a2):
    return math.factorial(a1) // (math.factorial(a1 - a2) * math.factorial(a2))

def f17(a1, a2, a3, a4):
    return ((a3 - a1) ** 2 + (a4 - a2) ** 2) ** 0.5

def f18(a1, a2):
    return (a1 + a2) % v1

def f19(a1):
    print(*a1, sep='\n')

def f20(a1):
    v1 = [True] * (a1 + 1)
    v1[0] = False
    v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if not v1[v2]:
            continue
        for v3 in range(v2 * 2, a1 + 1, v2):
            v1[v3] = False
    return v1
v3 = f2()
print(2 * v3 * math.pi)
