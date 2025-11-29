import numpy as np
(v1, v2), *v3 = [list(map(int, s.split())) for v4 in open(0)]
v5 = 100000000
v6 = np.full([2] * v1, v5, dtype=np.int)
v6[tuple([0] * v1)] = 0
for v7 in range(v2):
    v8 = v3[2 * v7][0]
    v9 = v3[2 * v7][1]
    v10 = v3[2 * v7 + 1]
    v11 = [slice(None)] * v1
    for v12 in v10:
        v11[v12 - 1] = slice(None, 1)
    v6 = np.minimum(v6, v6[tuple(v11)] + v8)
v13 = v6[tuple([1] * v1)]
if v13 == v5:
    print(-1)
else:
    print(v13)
