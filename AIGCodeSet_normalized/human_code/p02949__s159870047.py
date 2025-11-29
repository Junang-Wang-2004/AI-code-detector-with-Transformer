v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v2)]
v6 = float('inf')
v7 = [0] * 2 + [v6] * v1
for v5 in range(v1 - 1):
    for v8, v9, v10 in v4:
        v7[v9] = min(v7[v9], v7[v8] - v10 + v3)
v11 = v7[v1]
for v5 in range(v1):
    for v8, v9, v10 in v4:
        if v7[v9] > v7[v8] - v10 + v3:
            v7[v9] = -v6
print([max(-v7[v1], 0), -1][v7[v1] != v11])
