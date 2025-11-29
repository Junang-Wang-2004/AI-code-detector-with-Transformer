import numpy as np
v1, v2 = [int(a) for v3 in input().split()]
v4 = []
v5 = []
for v6 in range(v2):
    v7, v8 = [int(v3) for v3 in input().split()]
    v4.append(v7)
    v5.append(v8)
v9 = {}
id = ['' for v6 in range(len(v4))]
for v10 in np.argsort(v5):
    v9[v4[v10]] = v9.get(v4[v10], 0)
    id[v10] = '{0:06d}'.format(v4[v10]) + '{0:06d}'.format(v9[v4[v10]])
    v9[v4[v10]] += 1
for v10 in id:
    print(v10)
