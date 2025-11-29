v1, v2 = map(int, input().split())
v3 = [[0 for v4 in range(v2 + 1)] for v4 in range(10 ** 5 + 2)]
v5 = [0] * (10 ** 5 + 2)
for v4 in range(v1):
    v6, v7, v8 = map(int, input().split())
    v3[v6][v8] += 1
    v3[v7][v8] -= 1
for v9 in range(1, 10 ** 5 + 2):
    for v10 in range(1, v2 + 1):
        v3[v9][v10] += v3[v9 - 1][v10]
    v5[v9] = max(v5[v9 - 1], sum(v3[v9]))
print(max(v5))
