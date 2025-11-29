def f1():
    v1 = f2()
    v2 = 'ABC'
    if v1 >= 1000:
        v2 = 'ABD'
    print(v2)
import sys, copy, bisect, itertools, heapq, math
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque

def f2():
    return int(sys.stdin.readline())

def f3():
    return list(map(int, sys.stdin.readline().split()))

def f4():
    return list(map(str, sys.stdin.readline().split()))

def f5():
    return sys.stdin.readline().split()

def f6():
    return sys.stdin.readline().strip()
v1 = 10 ** 9 + 7
v2 = float('inf')
f1()
