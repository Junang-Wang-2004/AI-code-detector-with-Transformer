import numpy as np

def f1(a1):
    max = int(np.sqrt(a1))
    v1 = [i for v2 in range(2, a1 + 1)]
    v3 = []
    while v1[0] <= max:
        v3.append(v1[0])
        v4 = v1[0]
        v1 = [v2 for v2 in v1 if v2 % v4 != 0]
    v3.extend(v1)
    return v3
from itertools import accumulate
v1 = int(input())
v2 = [0] * v1
v3 = [0] * v1
v4 = f1(10 ** 5)
v5 = [0] * (10 ** 5 + 1)
v6 = [0] * (10 ** 5 + 1)
for v7 in range(10 ** 5):
    if v7 in v4:
        if (v7 + 1) // 2 in v4:
            v5[v7] = 1
v6 = list(accumulate(v5))
for v7 in range(v1):
    v2[v7], v3[v7] = map(int, input().split())
for v7 in range(v1):
    print(v6[v3[v7]] - v6[v2[v7] - 1])
