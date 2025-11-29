import numpy as np
v1, v2, v3 = map(int, input().split())
v4 = np.zeros(shape=v1, dtype='int64')
for v5 in range(v1):
    v6 = int(input())
    v4[v5] = v6

def f1(a1, a2):
    a2 -= a1 * v3
    a2 = (a2 - 1) // (v2 - v3) + 1
    return sum(a2[a2 > 0]) <= a1
v7 = 0
v8 = 10 ** 10
while v8 - v7 > 1:
    v9 = (v7 + v8) // 2
    if f1(v9, v4.copy()):
        v8 = v9
    else:
        v7 = v9
print(v8)
