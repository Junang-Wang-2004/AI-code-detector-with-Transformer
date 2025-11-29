v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = [0] * 31
for v6 in range(v1):
    for v7 in v3[v6][1:]:
        v5[v7] += 1
v8 = 0
for v9 in v5:
    if v9 == v1:
        v8 += 1
print(v8)
