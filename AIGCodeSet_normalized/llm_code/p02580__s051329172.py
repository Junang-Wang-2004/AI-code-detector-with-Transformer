v1, v2, v3 = map(int, input().split())
v4 = [0] * v1
v5 = [0] * v2
v6 = {}
for v7 in range(v3):
    v8, v9 = map(lambda x: int(x) - 1, input().split())
    v4[v8] += 1
    v5[v9] += 1
    v6[v8, v9] = 1
v10 = max(v4)
v11 = max(v5)
v12 = v10 + v11 - 1
v13 = [i for v14 in range(v2) if v5[v14] == v11]
for v8 in [v14 for v14 in range(v1) if v4[v14] == v10]:
    for v9 in v13:
        if (v8, v9) in v6:
            v12 = max(v12, v10 + v11 - 1)
            break
print(v12)
