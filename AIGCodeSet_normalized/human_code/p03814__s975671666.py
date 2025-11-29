def f1():
    v1 = f5()
    for v2, v3 in enumerate(v1):
        if v3 == 'A':
            v4 = v2
            break
    for v2, v3 in enumerate(v1[::-1]):
        if v3 == 'Z':
            v5 = v2
            break
    v6 = len(v1) - v4 - v5
    print(v6)
import sys
import copy
from collections import Counter, defaultdict, deque

def f2():
    return int(sys.stdin.readline())

def f3():
    return list(map(int, sys.stdin.readline().split()))

def f4():
    return sys.stdin.readline().split()

def f5():
    return sys.stdin.readline().strip()
v1 = 10 ** 9 + 7
v2 = float('inf')
f1()
