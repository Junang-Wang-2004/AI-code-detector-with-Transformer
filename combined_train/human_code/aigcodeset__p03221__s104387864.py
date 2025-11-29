from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from heapq import heappop, heappush, heappushpop, heapify
import copy
import numpy as np
import sys
v1 = float('inf')
v2 = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 6)

def f1(a1, a2):
    return a1 * a2 / gcd(a1, a2)

def f2():
    return list(map(int, sys.stdin.buffer.readline().split()))

def f3():
    return int(sys.stdin.buffer.readline())

def f4():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

def f5():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')

def f6(a1):
    return [f3() for v1 in range(a1)]

def f7(a1):
    return [f2() for v1 in range(a1)]

def f8(a1):
    return [f5() for v1 in range(a1)]

def f9(a1):
    return [f4() for v1 in range(a1)]

def f10(a1):
    return [list(f5()) for v1 in range(a1)]

def f11():
    v1, v2 = f2()
    v3 = [[] for v4 in range(v1)]
    v5 = [0 for v4 in range(v2)]
    for v4 in range(v2):
        v6, v7 = map(int, input().split())
        v3[v6 - 1].append((v7, v4))
    for v4 in range(v1):
        if len(v3[v4]) > 1:
            v3[v4].sort()
        for v8, v9 in enumerate(v3[v4]):
            v5[v9[1]] = str(v4 + 1).zfill(6) + str(v8 + 1).zfill(6)
    for v4 in range(v2):
        print(v5[v4])
if __name__ == '__main__':
    f11()
