from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
import numpy as np
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [[] for v4 in range(v1)]
for v6, v7, v8 in v3:
    v6 -= 1
    v7 -= 1
    v5[v6].append([v7, -v8])
v9 = [[np.inf] * v1 for v4 in range(v1)]

def f1(a1):
    v1 = [a1]
    v2 = [0] * v1
    v2[a1] = 1
    while v1:
        v3 = v1.pop()
        for v4, v5 in v5[v3]:
            if v2[v4] == 0:
                v2[v4] = 1
                v1.append(v4)
                v9[v3][v4] = v5
    return v2
v10 = f1(0)
v11 = [i for v12, v13 in enumerate(v10) if v13]
v14 = [-1] * v1
for v12, v13 in enumerate(v11):
    v14[v13] = v12
v15 = len(v11)
v16 = [[np.inf] * v15 for v4 in range(v15)]
for v12, v13 in enumerate(v11):
    for v17, v8 in enumerate(v9[v13]):
        if v14[v17] != -1:
            v16[v13][v14[v17]] = v8
try:
    v18 = csr_matrix(v16)
    v19 = bellman_ford(v18, indices=0)
    v20 = -int(v19[v1 - 1])
    print(v20)
except:
    print('inf')
