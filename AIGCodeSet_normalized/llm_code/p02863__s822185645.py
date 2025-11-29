v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append([v5, v6])
sorted(v3)
v7 = [[0] * 3005 for v8 in range(3005)]
v9 = 0
for v4 in range(v1):
    for v10 in range(v2):
        v7[v4 + 1][v10] = max(v7[v4 + 1][v10], v7[v4][v10])
        v11 = v10 + v3[v4][0]
        if v11 < v2:
            v7[v4 + 1][v11] = max(v7[v4 + 1][v11], v7[v4][v10] + v3[v4][1])
    v12 = v7[v4][v2 - 1] + v3[v4][1]
    v9 = max(v9, v12)
print(v9)
