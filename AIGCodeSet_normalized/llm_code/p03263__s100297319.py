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

def f5(a1):
    v1 = [tuple(map(int, f1().split())) for v2 in range(a1)]
    return map(list, zip(*v1))
v2, v3 = f3()
v4 = [f4() for v5 in range(v2)]
v6 = 0
v7 = []
for v8 in range(v2):
    for v9 in range(v3 - 1):
        if v4[v8][v9] % 2 == 1:
            v6 += 1
            v7.append([v8 + 1, v9 + 1, v8 + 1, v9 + 2])
for v8 in range(v2 - 1):
    if v4[v8][v3 - 1] % 2 == 1:
        v6 += 1
        v7.append([v8 + 1, v3, v8 + 2, v3])
print(v6)
for v8 in v7:
    print(*v8, sep=' ')
