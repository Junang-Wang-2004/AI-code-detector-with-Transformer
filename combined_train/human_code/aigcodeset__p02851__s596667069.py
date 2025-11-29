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
v2, v3 = f3()
v4 = [0] + f4()
v5 = []
v6 = 0
for v7, v8 in enumerate(v4):
    v6 += v8
    v5.append((v6 - v7) % v3)
v9 = defaultdict(int)
v10 = 0
for v7 in range(v2 + 1):
    v10 += v9[v5[v7]]
    v9[v5[v7]] += 1
    if v7 - v3 + 1 >= 0:
        v9[v5[v7 - v3 + 1]] -= 1
print(v10)
