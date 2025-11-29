from functools import reduce
from operator import mul

def f1(a1):
    v1 = []
    v2 = 2
    v3 = 0
    while v2 <= a1:
        v3 += a1 // v2
        v2 *= 2
    if v3 > 0:
        v1.append((2, v3))
    v4 = [1] * (a1 + 1)
    v5 = int(a1 ** 0.5) + 1
    for v6 in range(3, v5 + 1, 2):
        if v4[v6]:
            for v7 in range(v6 + v6, a1 + 1, v6):
                v4[v7] = 0
    for v6 in range(3, a1 + 1, 2):
        if v4[v6]:
            v2 = v6
            v3 = 0
            while v2 <= a1:
                v3 += a1 // v2
                v2 *= v6
            v1.append((v6, v3))
    return v1
import sys

def f2(*a1, **a2):
    print(*a1, file=sys.stderr, **a2)
v1 = [[74], [24, 2], [14, 4], [4, 4, 2]]
v2 = [1, 1, 1, 2]
v3 = int(input())
v4 = f1(v3)
v5 = [0] * (v3 + 1)
v6 = [0] * (v3 + 1)
for v4 in f1(v3):
    v5[v4[1]] += 1
for v7 in range(v3, -1, -1):
    v6[v7] = v5[v7] if v7 == v3 else v5[v7] + v6[v7 + 1]
v8 = 0
for v7, v9 in enumerate(v1):
    v10 = []
    for v11, v12 in enumerate(v9):
        if v12 > v3:
            break
        v10.append(v6[v12] - v11)
    if len(v10):
        v8 += reduce(mul, v10) // v2[v7]
print(v8)
