import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

def f1():
    return sys.stdin.readline()[:-1]
v1 = 10 ** 9 + 7

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return list(map(int, f1().split()))

def f5(a1, a2):
    if a1 <= 0:
        return [[]] * a2
    elif a2 == 1:
        return [f2() for v1 in range(a1)]
    else:
        v2 = [tuple(f3()) for v1 in range(a1)]
        return map(list, zip(*v2))

def f6(a1):
    v1 = 0
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            if a1 // v2 > v2 + 1:
                v1 += a1 // v2 - 1
    return v1
v2 = f2()
print(f6(v2))
