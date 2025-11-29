v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(8)]
for v4 in range(v1):
    v5 = list(map(int, input().split()))
    for v6 in range(8):
        v7 = 0
        v8 = v6
        v9 = [v6 // 4 % 2, v6 // 2 % 2, v6 % 2]
        for v10 in range(3):
            v7 += v5[v10] * (-1) ** v9[v10]
        v3[v6].append(v7)
for v11 in range(8):
    v3[v11].sort(reverse=True)
v12 = [sum(v3[v11][:v2]) for v11 in range(8)]
print(max(v12))
