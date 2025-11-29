import numpy as np
from itertools import product
v1 = int(input())
v2 = 10 ** 9 + 7
v3, v4, v5, v6 = range(1, 5)
v7 = np.zeros((v1 + 1, 5, 5, 5), dtype=np.int64)
v7[0, 0, 0, 0] = 1
for v8 in range(v1):
    for v9, v10, v11, v12 in product(range(5), range(5), range(5), range(1, 5)):
        if v9 == v3 and v10 == v4 and (v12 == v5):
            continue
        if v9 == v3 and v11 == v4 and (v12 == v5):
            continue
        if v10 == v3 and v11 == v4 and (v12 == v5):
            continue
        if v10 == v4 and v11 == v3 and (v12 == v5):
            continue
        if v10 == v3 and v11 == v5 and (v12 == v4):
            continue
        v7[v8 + 1, v10, v11, v12] += v7[v8, v9, v10, v11]
        v7[v8, v9, v10, v11] %= v2
v13 = 0
for v9, v10, v11 in product(range(1, 5), repeat=3):
    v13 += v7[v1, v9, v10, v11]
    v13 %= v2
print(v13)
