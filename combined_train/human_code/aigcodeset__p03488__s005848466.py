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
v2 = str(f1())
v3, v4 = f3()
v5 = len(v2)
v6 = []
v7 = []
v8 = True
v9 = 0
for v10 in range(v5):
    if v2[v10] == 'F':
        v9 += 1
    else:
        if v8:
            v6.append(v9)
            v8 = False
        else:
            v7.append(v9)
            v8 = True
        v9 = 0
if v9 != 0:
    if v8:
        v6.append(v9)
    else:
        v7.append(v9)
v6.append(0)
v7.append(0)
if v2[0] == 'F':
    v11 = True
else:
    v11 = False
v12 = sum(v6)
v13 = sum(v7)
if abs(v3) > v12 or abs(v4) > v13:
    print('No')
    exit()
v14 = [False] * (2 * v12 + 1)
v14[v12] = True
for v15, v16 in enumerate(v6):
    v17 = []
    if v15 == 0 and v11:
        v17.append(v12 + v16)
    else:
        for v10 in range(2 * v12 + 1):
            if v14[v10]:
                if 0 <= v10 + v16 <= 2 * v12:
                    v17.append(v10 + v16)
                if 0 <= v10 - v16 <= 2 * v12:
                    v17.append(v10 - v16)
    v14 = [False] * (2 * v12 + 1)
    for v18 in v17:
        v14[v18] = True
v19 = [False] * (2 * v13 + 1)
v19[v13] = True
for v20 in v7:
    v17 = []
    for v10 in range(2 * v13 + 1):
        if v19[v10]:
            if 0 <= v10 + v20 <= 2 * v13:
                v17.append(v10 + v20)
            if 0 <= v10 - v20 <= 2 * v13:
                v17.append(v10 - v20)
    v19 = [False] * (2 * v13 + 1)
    for v18 in v17:
        v19[v18] = True
if v14[v3 + v12] and v19[v4 + v13]:
    print('Yes')
else:
    print('No')
