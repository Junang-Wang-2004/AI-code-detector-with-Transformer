import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left
import heapq
import numpy as np

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

def f5():
    v1 = f1()
    v2 = f1()
    if len(set(v1) & set(v2)) != len(set(v2)):
        print(-1)
        exit()
    v3 = defaultdict(list)
    for v4, v5 in enumerate(v1):
        v3[v5].append(v4)
    v6 = 0
    v7 = -1
    for v4 in range(len(v2)):
        if len(v3[v2[v4]]) == 0:
            print(-1)
            exit()
        v8 = bisect_left(v3[v2[v4]], v7)
        if v8 != len(v3[v2[v4]]):
            v7 = v3[v2[v4]][v8] + 1
        else:
            v6 += 1
            v7 = -1
            v8 = bisect_left(v3[v2[v4]], v7)
            v7 = v3[v2[v4]][v8] + 1
    print(len(v1) * v6 + v7)
if __name__ == '__main__':
    f5()
