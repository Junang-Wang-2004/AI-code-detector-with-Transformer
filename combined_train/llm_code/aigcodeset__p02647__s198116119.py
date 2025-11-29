import numpy as np
import math
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = np.asarray(v3, dtype=int)
if v2 < int(math.exp(int(v1))):
    for v5 in range(v2):
        v6 = np.zeros(v1, dtype=int)
        for v7 in range(v1):
            v8 = v7 - v4[v7]
            v9 = v7 + v4[v7]
            if v8 < 0:
                v8 = 0
            if v9 >= v1:
                v9 = v1 - 1
            v6[v8:v9 + 1] += 1
        v4 = v6
    print(*v4)
else:
    v10 = np.zeros(v1, dtype=int)
    v10 += v1
    print(*v10)
