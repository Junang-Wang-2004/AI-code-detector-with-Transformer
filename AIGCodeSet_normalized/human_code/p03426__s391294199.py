v1, v2, v3 = list(map(int, input().split()))
v4 = [(0, 0) for v5 in range(v1 * v2 + 1)]
for v5 in range(1, v1 + 1):
    v6 = list(map(int, input().split()))
    for v7, v8 in enumerate(v6):
        v4[v8] = (v5, v7 + 1)
v9 = int(input())
v10 = []
v11 = []
v12 = [0] * (v1 * v2 + 1)
for v5 in range(v9):
    v13, v14 = list(map(int, input().split()))
    v10.append(v13)
    v11.append(v14)
for v5 in range(v3 + 1, v1 * v2 + 1):
    v12[v5] = v12[v5 - v3] + abs(v4[v5][0] - v4[v5 - v3][0]) + abs(v4[v5][1] - v4[v5 - v3][1])
for v5 in range(v9):
    print(v12[v11[v5]] - v12[v10[v5]])
