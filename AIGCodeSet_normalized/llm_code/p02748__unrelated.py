v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = []
for v7 in range(v3):
    v8, v9, v10 = map(int, input().split())
    v6.append([v8, v9, v10])
v11 = v4[0] + v5[0]
for v12 in range(v1):
    for v13 in range(v2):
        v14 = v4[v12] + v5[v13]
        for v8, v9, v10 in v6:
            if v12 + 1 == v8 and v13 + 1 == v9:
                v14 = min(v14, v4[v12] + v5[v13] - v10)
        v11 = min(v11, v14)
print(v11)
