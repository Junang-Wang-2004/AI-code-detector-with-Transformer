import numpy as np
v1 = input()
v2 = len(v1)
v3 = []
v4 = 'R'
v5 = 1
for v6 in range(1, v2):
    if v1[v6] != v4:
        v3.append(v5)
        v5 = 1
        v4 = v1[v6]
    else:
        v5 += 1
v3.append(v5)
v7 = []
for v6 in range(0, len(v3), 2):
    v8, v9 = (0, 0)
    v10, v11 = (v3[v6], v3[v6 + 1])
    v8 += v10 // 2
    v9 += v10 // 2
    if v10 % 2 == 1:
        v8 += 1
    v8 += v11 // 2
    v9 += v11 // 2
    if v11 % 2 == 1:
        v9 += 1
    v7 += list(np.zeros(v10 - 1, dtype=int)) + [v8, v9] + list(np.zeros(v11 - 1, dtype=int))
for v6 in v7:
    print(v6, end=' ')
print()
