v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v2 + 1)]
v5 = [list(map(int, input().split())) for v6 in range(v1)]
v5.sort(key=lambda x: x[0])
v4 = 0
for v7 in range(1, v2 + 1):
    while v4 < v1 and v5[v4][0] <= v7:
        v8, v9 = v5[v4]
        for v10 in range(v2, v9 - 1, -1):
            v3[v10] = max(v3[v10], v3[v10 - v9] + v8)
        v4 += 1
    v3[v7] = max(v3[v7], v3[v7 - 1])
print(v3[v2])
