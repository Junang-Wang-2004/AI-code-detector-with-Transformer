import sys
v1 = sys.stdin
sys.setrecursionlimit(10 ** 7)

def f1():
    return map(int, v1.readline().split())

def f2():
    return map(lambda x: int(x) - 1, v1.readline().split())

def f3():
    return map(float, v1.readline().split())

def f4():
    return v1.readline().split()

def f5():
    return v1.readline().rstrip()

def f6():
    return list(f5())

def f7():
    return int(v1.readline())

def f8():
    return float(v1.readline())
from heapq import heappush, heappop

def f9(a1: list, a2, a3=float('inf')) -> list:
    v1 = len(a1)
    v2 = [a3] * v1
    v3 = [False] * v1
    v2[a2] = 0
    v4 = [(0, a2)]
    while v4:
        v5, v6 = heappop(v4)
        if v3[v6]:
            continue
        v3[v6] = True
        for v7, v8 in a1[v6]:
            v9 = v5 + v8
            if v9 < v2[v7]:
                v2[v7] = v9
                heappush(v4, (v9, v7))
    return v2
v2, v3, v4 = f1()
v5 = [[] for v6 in range(v2)]
v7 = [[] for v6 in range(v2)]
for v6 in range(v3):
    v8, v9, v10 = f1()
    v8 -= 1
    v9 -= 1
    v5[v8].append((v9, v10))
    v5[v9].append((v8, v10))
for v11 in range(v2):
    v12 = f9(v5, v11)
    for v13 in range(v2):
        if v11 == v13:
            continue
        if v12[v13] <= v4:
            v7[v11].append((v13, 1))
v14 = f7()
v15 = float('inf')
v12 = [[v15] * v2 for v6 in range(v2)]
for v16 in range(v2):
    v12[v16] = f9(v7, v16, v15)
for v6 in range(v14):
    v11, v13 = f2()
    if v12[v11][v13] == v15:
        print(-1)
    else:
        print(v12[v11][v13] - 1)
