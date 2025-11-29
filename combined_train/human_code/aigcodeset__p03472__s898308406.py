import numpy as np
v1, v2 = map(int, input().split())
v3 = [input().split() for v4 in range(v1)]
v5 = [int(v3[v4][0]) for v4 in range(v1)]
v6 = max(v5)
v7 = np.array([int(v3[v4][1]) for v4 in range(v1)])
v8 = v7[v7 > v6]
v9 = 0
if sum(v8) < v2:
    v10 = len(v8)
    v11 = v2 - sum(v8)
    if v11 % v6 == 0:
        v9 = v11 // v6
    else:
        v9 = v11 // v6 + 1
else:
    v7 = np.sort(v8)[::-1]
    v12 = 0
    for v4 in range(len(v7)):
        v12 += v7[v4]
        if v12 >= v2:
            v10 = v4 + 1
            v9 = 0
            break
print(v10 + v9)
