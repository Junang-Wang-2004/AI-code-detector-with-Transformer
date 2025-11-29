import numpy as np
import math

def f1(a1, a2, a3, a4, a5):
    if a1 == a2:
        return a1
    v1 = (a2 + a1) // 2
    v2 = a5 - v1 * a4
    if len(v2) == 0:
        return f1(a1, v1, a3, a4, a5)
    v2 = np.maximum(v2, 0)
    v2 = np.ceil(v2 / (a3 - a4))
    v3 = np.sum(v2)
    if v3 <= v1:
        return f1(a1, v1, a3, a4, a5)
    else:
        return f1(v1 + 1, a2, a3, a4, a5)
v1, v2, v3 = list(map(int, input().split()))
v4 = []
for v5 in range(v1):
    v6 = int(input())
    v4.append(v6)
v4 = sorted(v4, reverse=True)
v4 = np.array(v4)
v7 = v4[0] // v3 + 1
v8 = v4[-1] // v2
v9 = f1(v8, v7, v2, v3, v4)
print(v9)
