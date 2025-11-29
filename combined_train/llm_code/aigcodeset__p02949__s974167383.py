v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v4.append((v6, v7, v8))
v9 = float('inf')
v10 = [v9] * (v1 + 1)
v10[1] = 0
for v5 in range(v1 - 1):
    for v11 in v4:
        v12, v13, v14 = v11
        if v10[v12] + v14 < v10[v13]:
            v10[v13] = v10[v12] + v14
for v11 in v4:
    v12, v13, v14 = v11
    if v10[v12] + v14 < v10[v13]:
        if v13 == v1:
            print(-1)
            exit()
        v10[v13] = v10[v12] + v14
print(max(v10[v1] - v3 * (v1 - 1), 0))
