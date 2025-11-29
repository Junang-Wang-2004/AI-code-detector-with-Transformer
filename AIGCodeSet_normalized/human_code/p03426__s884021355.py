v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(list(map(int, input().split())))
v6 = int(input())
v7 = []
v8 = []
for v5 in range(v6):
    v9, v10 = map(int, input().split())
    v7.append(v9)
    v8.append(v10)
v11 = dict()
for v12, v13 in enumerate(v4):
    for v14, v15 in enumerate(v13):
        v11[v15] = (v14, v12)
v16 = [[] for v17 in range(v3)]
for v5 in range(v1 * v2):
    v5 += 1
    v16[v5 % v3].append(v11[v5])
v18 = [[0] for v17 in range(v3)]
for v5 in range(v3):
    for v19 in range(1, len(v16[v5])):
        v18[v5].append(v18[v5][v19 - 1] + abs(v16[v5][v19 - 1][0] - v16[v5][v19][0]) + abs(v16[v5][v19 - 1][1] - v16[v5][v19][1]))
for v5 in range(v6):
    v20 = v18[v7[v5] % v3]
    v21 = (v7[v5] - 1) // v3
    v22 = (v8[v5] - 1) // v3
    print(v20[v22] - v20[v21])
