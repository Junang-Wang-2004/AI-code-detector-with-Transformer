import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools
from collections import deque
sys.setrecursionlimit(10 ** 7)
v1 = 10 ** 20
v2 = 10 ** 9 + 7
v3 = [1, -1, 0, 0]
v4 = [0, 0, 1, -1]

def f1():
    return [int(x) for v1 in sys.stdin.readline().split()]

def f2():
    return [int(x) - 1 for v1 in sys.stdin.readline().split()]

def f3():
    return [float(x) for v1 in sys.stdin.readline().split()]

def f4():
    return sys.stdin.readline().split()

def f5():
    return int(sys.stdin.readline())

def f6():
    return float(sys.stdin.readline())

def f7():
    return input()

def f8():
    v1, v2 = f1()
    v3 = []
    v4 = [0 for v5 in range(v1)]
    v6 = 0
    for v7 in range(1, v2 + 1):
        while v4[v6] or v4[(v6 + v7) % v1]:
            v6 += 1
        v3.append((v6, (v6 + v7) % v1))
        v4[v6] = 1
        v4[(v6 + v7) % v1] = 1
    for v8 in v3:
        print(v8[0] + 1, v8[1] + 1)
f8()
