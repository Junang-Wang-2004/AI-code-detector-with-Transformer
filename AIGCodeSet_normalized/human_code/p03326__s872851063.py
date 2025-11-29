v1, v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v5, v6, v7 = list(map(int, input().split()))
    v3.append([v5, v6, v7])
v8 = 0
for v4 in range(8):
    v9 = v4 % 2
    v10 = v4 // 2
    v11 = v10 % 2
    v12 = v10 // 2
    v13 = v12 % 2
    v9, v11, v13 = (2 * v9 - 1, 2 * v11 - 1, 2 * v13 - 1)
    v14 = []
    for v10 in range(v1):
        v14.append(v9 * v3[v10][0] + v11 * v3[v10][1] + v13 * v3[v10][2])
    v14.sort(reverse=True)
    v8 = max(sum(v14[:v2]), v8)
print(v8)
