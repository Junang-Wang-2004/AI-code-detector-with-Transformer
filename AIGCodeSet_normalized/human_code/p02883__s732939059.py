import numpy as np
v1, v2 = map(int, input().split())
v3 = np.array(input().split(), np.int64)
v4 = np.array(input().split(), np.int64)
v3.sort()
v4.sort()
v4 = v4[::-1]
v5 = v3.sum()
v6, v7 = (-1, max(v3) * max(v4))
while v6 + 1 < v7:
    v8 = (v6 + v7) // 2
    if np.minimum(v3, v8 // v4).sum() >= v5 - v2:
        v7 = v8
    else:
        v6 = v8
print(v7)
