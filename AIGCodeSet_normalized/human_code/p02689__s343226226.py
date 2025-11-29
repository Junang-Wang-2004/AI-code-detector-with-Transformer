import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10 ** 7)

def f1():
    return sys.stdin.readline()[:-1]
v1 = 10 ** 9 + 7

def f2():
    return int(f1())

def f3():
    return list(map(int, f1().split()))

def f4(a1, a2):
    if a1 <= 0:
        return [[] for v1 in range(a2)]
    elif a2 == 1:
        return [f2() for v1 in range(a1)]
    else:
        v2 = [f3() for v1 in range(a1)]
        return map(list, zip(*v2))

def f5(a1, a2, a3, a4=False):
    v1 = [[] for v2 in range(a3)]
    for v3 in range(len(a1)):
        v1[a1[v3] - 1].append(a2[v3] - 1)
        if not a4:
            v1[a2[v3] - 1].append(a1[v3] - 1)
    return v1
v2, v3 = f3()
v4 = f3()
v5, v6 = f4(v3, 2)
v7 = f5(v5, v6, v2)
v8 = 0
v9 = [False] * v2
for v10 in range(v2):
    v11 = True
    if not v9[v10]:
        for v12 in v7[v10]:
            if v4[v12] > v4[v10]:
                v9[v10] = True
                v11 = False
                break
            elif v4[v12] == v4[v10]:
                v11 = False
                v9[v12] = True
            else:
                v9[v12] = True
    if v9[v10]:
        v11 = False
    if v11:
        v8 += 1
print(v8)
