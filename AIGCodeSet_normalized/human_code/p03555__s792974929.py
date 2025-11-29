from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect

def f1():
    return list(map(int, sys.stdin.readline().split()))

def f2():
    return int(sys.stdin.readline())

def f3():
    return sys.stdin.readline().split()

def f4():
    return list(sys.stdin.readline())

def f5(a1):
    return [f2() for v1 in range(a1)]

def f6(a1):
    return [f1() for v1 in range(a1)]

def f7(a1):
    return [f4() for v1 in range(a1)]

def f8(a1):
    return [f3() for v1 in range(a1)]
v1 = 1000000007
v2 = input()
v3 = input()
if v2[2] == v3[0] and v2[1] == v3[1] and (v2[0] == v3[2]):
    print('YES')
else:
    print('NO')
