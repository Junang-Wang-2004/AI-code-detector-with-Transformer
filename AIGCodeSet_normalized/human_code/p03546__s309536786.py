v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(10)]
for v5 in range(10):
    for v6 in range(10):
        for v7 in range(10):
            v3[v6][v7] = min(v3[v6][v7], v3[v6][v5] + v3[v5][v7])
v8 = {v6: 0 for v6 in range(-1, 10)}
for v4 in range(v1):
    v9 = map(int, input().split())
    for v6 in v9:
        v8[v6] += 1
v10 = 0
for v6 in range(10):
    if v6 == 1:
        continue
    v10 += v3[v6][1] * v8[v6]
print(v10)
