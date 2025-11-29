v1, v2, v3 = map(int, input().split())
from itertools import product
v4, v5, v6, v7 = ([], [], [], [])
for v8 in range(v3):
    v9, v10, v11, v12 = map(int, input().split())
    v4.append(v9 - 1)
    v5.append(v10 - 1)
    v6.append(v11)
    v7.append(v12)
v13 = 0
v14 = [v8 + 1 for v8 in range(v2)]
for v15 in product(v14, repeat=v1):
    if v15[0] <= v15[1] <= ... <= v15[v1 - 1]:
        v16 = 0
        for v8 in range(v3):
            if v15[v5[v8]] - v15[v4[v8]] == v6[v8]:
                v16 += v7[v8]
        v13 = max(v13, v16)
print(v13)
