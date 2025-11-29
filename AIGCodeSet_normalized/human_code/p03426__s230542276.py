v1, v2, v3 = map(int, input().split())
v4 = [0] * (v1 * v2 + 1)
v4[0] = (-1, -1)
for v5 in range(v1):
    v6 = list(map(int, input().split()))
    for v7 in range(v2):
        v4[v6[v7]] = (v5, v7)
v8 = int(input())
v9 = [0] * (v1 * v2 + 1)
for v10 in range(v3 + 1, v1 * v2 + 1):
    v11, v12 = v4[v10]
    v13, v14 = v4[v10 - v3]
    v9[v10] = v9[v10 - v3] + abs(v11 - v13) + abs(v12 - v14)
for v10 in range(v8):
    v15, v16 = map(int, input().split())
    print(v9[v16] - v9[v15])
