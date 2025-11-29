import numpy as np
v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = []
for v7 in range(v3):
    v8 = list(map(int, input().split()))
    v6.append(v8)
v9 = min(v4) + min(v5)
for v7 in v6:
    v10 = v4[v7[0] - 1] + v5[v7[1] - 1] - v7[2]
    if v9 > v10:
        v9 = v10
print(v9)
