import sys
sys.setrecursionlimit(10 ** 6)
from math import floor, ceil, sqrt, factorial, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
v1 = 10 ** 9 + 7
v2 = float('inf')
v3 = -float('inf')

def f1():
    return int(sys.stdin.readline().rstrip())

def f2():
    return map(int, sys.stdin.readline().rstrip().split())

def f3():
    return list(f2())

def f4(a1: int):
    return [f1() for v1 in range(a1)]

def f5(a1: int):
    return [f3() for v1 in range(a1)]

def f6():
    return sys.stdin.readline().rstrip()

def f7():
    return sys.stdin.readline().rstrip().split()

def f8():
    return list(f7())

def f9(a1: int):
    return [f6() for v1 in range(a1)]

def f10(a1: int):
    return [f8() for v1 in range(a1)]
v4 = f1()
v5 = f3()
v6 = []
while len(v5) > 0:
    v7 = False
    v8 = 0
    for v9, v10 in enumerate(v5):
        if v9 + 1 == v10:
            v8 = v10 - 1
            v7 = True
    v11 = v5.pop(v8)
    v6.append(v11)
    if v7 == False:
        print(-1)
        exit()
v12 = reversed(v6)
for v9, v10 in enumerate(v12):
    print(v10)
