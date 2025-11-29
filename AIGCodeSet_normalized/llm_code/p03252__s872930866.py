from math import ceil, floor, comb, factorial, gcd, pow, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)

def f1():
    return sys.stdin.readline().strip()

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return list(f3())
v1 = f1()
v2 = f1()
v3 = [0] * (ord('z') + 1)
v4 = [0] * (ord('z') + 1)
for v5 in range(len(v1)):
    v6 = ord(v1[v5])
    v7 = ord(v2[v5])
    v3[v6] = v7
    v4[v7] = v6
if Counter(v3) == Counter(v4):
    print('Yes')
else:
    print('No')
