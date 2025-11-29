v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort(key=lambda x: x[0])
v5 = [0] * (v2 + 1)
for v6 in range(v1):
    v7, v8 = v3[v6]
    for v9 in range(v2, v7 - 1, -1):
        v5[v9] = max(v5[v9], v5[v9 - v7] + v8)
print(v5[v2])
