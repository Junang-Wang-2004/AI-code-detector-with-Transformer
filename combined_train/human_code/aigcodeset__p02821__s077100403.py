import sys
import math
import cmath
sys.setrecursionlimit(1000000)

def f1(a1, a2):
    if a2 == 1:
        return
    v1 = a2 // 2
    v2 = [a1[2 * i] for v3 in range(v1)]
    v4 = [a1[2 * v3 + 1] for v3 in range(v1)]
    f1(v2, v1)
    f1(v4, v1)
    f2(a1, v2, v4, a2)
    return

def f2(a1, a2, a3, a4):
    v1 = a4 // 2
    for v2 in range(a4):
        v3 = cmath.exp(2j * v2 * cmath.pi / a4)
        a1[v2] = a2[v2 % v1] + v3 * a3[v2 % v1]
    return

def f3(a1, a2):
    if a2 == 1:
        return
    v1 = a2 // 2
    v2 = [a1[2 * i] for v3 in range(v1)]
    v4 = [a1[2 * v3 + 1] for v3 in range(v1)]
    f3(v2, v1)
    f3(v4, v1)
    f4(a1, v2, v4, a2)
    return

def f4(a1, a2, a3, a4):
    v1 = a4 // 2
    for v2 in range(a4):
        v3 = cmath.exp(-2j * v2 * cmath.pi / a4)
        a1[v2] = a2[v2 % v1] + v3 * a3[v2 % v1]
    return

def f5(a1, a2):
    v1, v2 = (len(a1), len(a2))
    v3 = 2 ** (int(math.log2(v1 + v2)) + 1)
    for v4 in range(v3 - v1):
        a1.append(0)
    for v4 in range(v3 - v2):
        a2.append(0)
    f1(a1, v3)
    f1(a2, v3)
    v5 = [a1[v4] * a2[v4] for v4 in range(v3)]
    f3(v5, v3)
    v6 = [round(v5[v4].real / v3) for v4 in range(v3)]
    return (v6, v3)
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = max(v3)
v5 = [0] * (v4 + 1)
v6 = [0] * (v4 + 1)
for v7 in v3:
    v5[v7] += 1
    v6[v7] += 1
v8, v9 = f5(v5, v6)
v10 = 0
v11 = 0
for v7 in range(min(200000, v9 - 1), -1, -1):
    if v8[v7] + v10 >= v2:
        v11 += (v2 - v10) * v7
        v10 += v2 - v10
    else:
        v11 += v8[v7] * v7
        v10 += v8[v7]
    if v10 == v2:
        break
print(v11)
