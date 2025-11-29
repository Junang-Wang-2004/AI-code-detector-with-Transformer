import numpy as np
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(int(input()))

def f1(a1):
    v1 = np.array(v4)
    v1 -= v3 * a1
    v2 = 0
    for v3 in v1:
        v2 += max((v3 - 1) // (v2 - v3) + 1, 0)
    return v2 <= a1
v6 = 0
v7 = 10 ** 9
while v6 + 1 < v7:
    v8 = (v6 + v7) // 2
    if f1(v8):
        v7 = v8
    else:
        v6 = v8
print(v7)
