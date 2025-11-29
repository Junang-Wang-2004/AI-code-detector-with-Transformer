import sys
import math
import heapq
sys.setrecursionlimit(10 ** 7)
v1 = 9223372036854775807
v2 = -9223372036854775808
v3 = 1000000007

def f1(a1, a2):
    return pow(a1, a2, v3)

def f2(a1, a2=v3):
    return pow(a1, a2 - 2, a2)

def f3(a1, a2, a3=v3):
    return a1 * f2(a2, a3) % a3

def f4():
    return [int(x) for v1 in input().split()]

def f5():
    return [float(x) for v1 in input().split()]

def f6():
    return input().split()

def f7():
    return int(input())

def f8(a1):
    v1 = [1]
    for v2 in range(1, a1 + 1):
        v1.append(v1[v2 - 1] * v2 % v3)
    return v1

def f9(a1, a2):
    if a1 < a2:
        a1, a2 = (a2, a1)
    v3 = a1 % a2
    while v3 != 0:
        a1, a2 = (a2, v3)
        v3 = a1 % a2
    return a2
v4 = f7()
v5 = [[(0, 0) for v6 in range(v4 - 1)] for v6 in range(v4)]
for v7 in range(v4):
    v8 = f4()
    for v9 in range(v4 - 1):
        if v7 + 1 < v8[v9]:
            v5[v7][v9] = (v7 + 1, v8[v9])
        else:
            v5[v7][v9] = (v8[v9], v7 + 1)
v10 = True
v11 = [0] * v4
v12 = 0
v13 = set()
v14 = range(v4)
while v10:
    v15 = False
    v16 = []
    for v7 in v14:
        if v11[v7] < v4 - 1:
            v17 = v5[v7][v11[v7]]
            v18, v19 = v17
            if v17 in v13:
                v13.remove(v17)
                if v11[v7] < v4 - 1:
                    v11[v18 - 1] += 1
                    v11[v19 - 1] += 1
                    v15 = True
                    v16.append(v18 - 1)
                    v16.append(v19 - 1)
            else:
                v13.add(v17)
    v14 = v16
    v10 = v15
    v12 += v15
if sum(v11) == v4 * (v4 - 1):
    print(v12)
else:
    print(-1)
