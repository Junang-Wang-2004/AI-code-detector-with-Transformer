v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = [0] * (v2 + 1)
for v6 in range(v1):
    for v7 in range(1, v3[v6][0] + 1):
        v5[v3[v6][v7]] += 1
v8 = 0
for v6 in range(v2 + 1):
    if v5[v6] == v1:
        v8 += 1
print(v8)
