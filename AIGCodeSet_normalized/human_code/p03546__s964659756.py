v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(10)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
for v6 in range(10):
    for v7 in range(10):
        for v8 in range(10):
            v3[v7][v8] = min(v3[v7][v8], v3[v7][v6] + v3[v6][v8])
v9 = 0
for v7 in range(v1):
    for v8 in range(v2):
        if v5[v7][v8] >= 0:
            v9 += v3[v5[v7][v8]][1]
print(v9)
