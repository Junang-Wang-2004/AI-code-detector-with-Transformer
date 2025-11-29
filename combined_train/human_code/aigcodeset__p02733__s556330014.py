v1, v2, v3 = (int(x) for v4 in input().split())
v5 = [input() for v6 in range(v1)]
v7 = 10 ** 18
for v8 in range(1 << v1 - 1):
    v9 = [0] * v1
    v10 = 0
    for v11 in range(v1 - 1):
        if v8 & 1 << v11:
            v10 += 1
        v9[v11 + 1] = v10
    v12 = max(v9) + 1
    v13 = v12 - 1
    v14 = [0] * v12
    for v15 in range(v2):
        v16 = [0] * v12
        for v11 in range(v1):
            v14[v9[v11]] += int(v5[v11][v15])
            v16[v9[v11]] += int(v5[v11][v15])
            if v14[v9[v11]] > v3:
                v13 += 1
                for v17 in range(v12):
                    v14[v17] = v16[v17]
    v7 = min(v7, v13)
print(v7)
