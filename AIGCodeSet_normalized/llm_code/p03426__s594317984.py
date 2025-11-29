v1, v2, v3 = map(int, input().split())
v4 = []
v5 = [0 for v6 in range(v1 * v2 + 1)]
for v7 in range(v1):
    v4.append(list(map(int, input().split())))
for v8 in range(v1):
    for v9 in range(v2):
        v5[v4[v8][v9]] = (v8, v9)
v7 = [0 for v6 in range(v1 * v2 + 1)]
for v8 in range(v3):
    v10 = 0
    for v9 in range(v8, v1 * v2, v3):
        if v9 != v8:
            v11 = (v5[v9 + 1][0], v5[v9 + 1][1])
            v12 = (v5[v9 + 1 - v3][0], v5[v9 + 1 - v3][1])
            v10 += abs(v11[0] - v12[0]) + abs(v11[1] - v12[1])
        v7[v9 + 1] = v10
v13 = int(input())
for v6 in range(v13):
    v14, v15 = map(int, input().split())
    print(v7[v15] - v7[v14])
