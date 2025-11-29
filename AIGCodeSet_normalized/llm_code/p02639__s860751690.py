import sys, io, os, re
import bisect
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor
from copy import copy, deepcopy
from collections import deque
from fractions import gcd
from functools import reduce
from itertools import groupby
v1 = lambda: int(sys.stdin.readline().strip())
v2 = lambda: list(map(int, sys.stdin.readline().strip().split()))
v3 = lambda: float(sys.stdin.readline().strip())
v4 = lambda: list(map(float, sys.stdin.readline().strip().split()))
v5 = lambda: sys.stdin.readline().strip()
v6 = lambda: list(sys.stdin.readline().strip().split())
v7 = lambda n: [v1() for v8 in range(n)]
v9 = lambda n: [v3() for v8 in range(n)]
v10 = lambda n: [v5() for v8 in range(n)]
v11 = lambda n: [v2() for v8 in range(n)]
v12 = lambda n: [v4() for v8 in range(n)]
v13 = lambda n: [v6() for v8 in range(n)]

def f1(a1):
    return [0] * a1

def f2(a1, a2):
    return [[0] * a2 for v1 in range(a1)]

def f3(a1, a2, a3):
    return [[[0] * a3 for v1 in xrange(a2)] for v2 in xrange(a1)]
v14 = v2()
for v15 in range(len(v14)):
    if v14[v15] == 0:
        print(v15 + 1)
