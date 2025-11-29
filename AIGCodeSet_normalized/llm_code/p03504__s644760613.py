v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = [0] * (10 ** 5 + 1)
for v6, v7, v8 in v3:
    v5[v6] += 1
    v5[v7] -= 1
v9 = v5[0]
for v10 in range(1, 10 ** 5 + 1):
    v5[v10] += v5[v10 - 1]
    if v5[v10] > v9:
        v9 = v5[v10]
print(v9)
