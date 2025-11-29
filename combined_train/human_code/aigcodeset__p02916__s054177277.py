v1 = 10 ** 9 + 7
import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
from itertools import combinations
import bisect

def f1():
    return map(int, sys.stdin.readline().split())

def f2():
    return int(sys.stdin.readline().rstrip())

def f3():
    return sys.stdin.readline().rstrip()
v2 = f2()
v3 = [list(f1()) for v4 in range(3)]
v5 = 0
for v6 in range(v2 - 1):
    v5 += v3[1][v3[0][v6] - 1]
    if v3[0][v6] + 1 == v3[0][v6 + 1]:
        v5 += v3[2][v3[0][v6] - 1]
print(v5 + v3[1][v3[0][v2 - 1] - 1])
