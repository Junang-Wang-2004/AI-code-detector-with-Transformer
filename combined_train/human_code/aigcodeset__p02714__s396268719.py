"""
import random
import functools
import copy
import bisect
import array
import re
import collections
import heapq
import fractions
import itertools
import string
import math
from operator import itemgetter as ig
from bisect import bisect_left, bisect_right, insort_left, insort_right
from itertools import permutations, combinations, product, accumulate, groupby
from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10 ** 7)
# import numpy as np

inf = 10 ** 20
INF = float("INF")
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
'''for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:'''
"""
from collections import Counter
import sys
sys.setrecursionlimit(10 ** 7)

def f1():
    return list(map(int, sys.stdin.readline().split()))

def f2():
    return [int(x) - 1 for v1 in sys.stdin.readline().split()]

def f3():
    return sys.stdin.readline().split()

def f4():
    return int(sys.stdin.readline())

def f5():
    return input()

def f6(a1):
    return [f4() for v1 in range(a1)]

def f7(a1):
    return [f5() for v1 in range(a1)]

def f8():
    return list(input())

def f9(a1):
    return [f1() for v1 in range(a1)]

def f10(a1):
    return [f2() for v1 in range(a1)]

def f11(a1):
    return [f3() for v1 in range(a1)]

def f12(a1):
    return [[int(i) for v1 in sys.stdin.readline().split()[0]] for v2 in range(a1)]

def f13(a1):
    return [f8() for v1 in range(a1)]

def f14(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f15():
    v1 = f4()
    v2 = f5()
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    for v7 in range(v1):
        if v2[v7] == 'R':
            v3 += 1
        elif v2[v7] == 'B':
            v5 += 1
        elif v2[v7] == 'G':
            v4 += 1
    v6 = v3 * v4 * v5
    for v7 in range(v1 - 2):
        for v8 in range(v7 + 1, v1 - 1):
            if v2[v7] != v2[v8] and 2 * v8 - v7 < v1 and (v2[v7] != v2[2 * v8 - v7]) and (v2[v8] != v2[2 * v8 - v7]):
                v6 -= 1
    print(v6)
if __name__ == '__main__':
    f15()
