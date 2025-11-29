v1, v2 = map(int, input().split())
v3, v4 = ([], [])
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = [[0, 0] for v5 in range(v2)]
for v5 in range(v1):
    for v9 in reversed(range(v2)):
        v8[v9][1] = max(v8[v9][1], v8[v9][0] + v4[v5])
        if v9 - v3[v5] >= 0:
            v8[v9][0] = max(v8[v9 - v3[v5]][0] + v4[v5], v8[v9][0])
            v8[v9][1] = max(v8[v9 - v3[v5]][1] + v4[v5], v8[v9][1])
v10 = max(v8[v2 - 1][0], v8[v2 - 1][1])
print(v10)
