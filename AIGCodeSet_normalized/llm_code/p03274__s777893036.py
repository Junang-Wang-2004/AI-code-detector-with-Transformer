import numpy as np
v1 = 10 ** 9
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = [0] + [v1] * v3
v6 = [0] + [v1] * v3
v7, v8 = (1, 1)
for v9 in range(v2):
    if v4[v9] >= 0 and v7 < v3 + 1:
        v5[v7] = v4[v9]
        v7 += 1
    elif v4[v9] < 0 and v8 < v3 + 1:
        v6[v8] = -v4[v9]
        v8 += 1
v6.sort(reverse=True)
v10 = v1 * 3
for v9 in range(v3 + 1):
    v11 = v5[v9] + 2 * v6[v9]
    v10 = min(v10, v11)
    v11 = 2 * v5[v9] + v6[v9]
    v10 = min(v10, v11)
print(v10)
