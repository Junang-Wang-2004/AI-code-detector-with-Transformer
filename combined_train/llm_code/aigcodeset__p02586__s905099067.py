v1, v2, v3 = map(int, input().split())
v4 = [[-float('inf')] * v2 for v5 in range(v1)]
for v6 in range(v3):
    v7, v8, v9 = map(int, input().split())
    v7 -= 1
    v8 -= 1
    v4[v7][v8] = v9
v4[v1 - 1][v2 - 1] = max(0, v4[v1 - 1][v2 - 1])
v10 = [[(0, 0, float('inf'))] * (v2 + 1) for v5 in range(v1 + 1)]
for v7 in range(v1):
    for v8 in range(v2):
        if v4[v7][v8] <= 0:
            continue
        v11, v12, v13 = v10[v7][v8]
        if v7 + 1 < v1 and v4[v7 + 1][v8] >= 0:
            if v10[v7 + 1][v8][0] < v11 + v4[v7][v8]:
                v10[v7 + 1][v8] = (v11 + v4[v7][v8], 0, v4[v7 + 1][v8])
        if v8 + 1 < v2 and v4[v7][v8 + 1] >= 0:
            if v10[v7][v8 + 1][0] < v11 + v4[v7][v8]:
                if v12 < 3:
                    v10[v7][v8 + 1] = (v11 + v4[v7][v8], v12 + 1, min(v13, v4[v7][v8 + 1]))
                else:
                    v14 = v11 + v4[v7][v8] - min(v13, v4[v7][v8 + 1])
                    if v10[v7][v8 + 1][0] < v14:
                        v10[v7][v8 + 1] = (v14, v12 + 1, min(v13, v4[v7][v8 + 1]))
print(v10[v1 - 1][v2 - 1][0] + v4[v1 - 1][v2 - 1])
