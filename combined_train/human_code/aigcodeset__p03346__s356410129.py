import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10 ** 7)
v1 = 0
v2 = 0
v3 = 10 ** 20
v4 = float('INF')
v5 = 1.0 / 10 ** 10
v6 = 10 ** 9 + 7
v7 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
v8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

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
    return [f4() - 1 for v1 in range(a1)]

def f8(a1):
    return [f5() for v1 in range(a1)]

def f9(a1):
    return [f1() for v1 in range(a1)]

def f10(a1):
    return [f2() for v1 in range(a1)]

def f11(a1):
    return [f3() for v1 in range(a1)]
v9 = f4()
v10 = f7(v9)
v11 = set()
v12 = [0] * v9
for v13 in range(v9):
    if v10[v13] - 1 in v11:
        if v10[v13] != 0:
            v12[v10[v13] - 1] = 1
    v11.add(v10[v13])
v14 = 1 if v12[0] == 1 else 0
v2 = 1 if v12[0] == 1 else 0
for v13 in range(1, v9):
    if v14 == 1:
        if v12[v13] == 1:
            v2 += 1
        else:
            v14 = 0
            v1 = max(v1, v2)
            v2 = 0
    elif v12[v13] == 1:
        v2 += 1
        v14 = 1
    else:
        pass
v1 = max(v1, v2) + 1
print(v9 - v1)
