v1, v2 = list(map(int, input().split()))
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
v6 = [[0 for v4 in range(v2)] for v4 in range(3)]
for v7 in range(v1):
    for v8 in range(v1):
        v9 = v5[v7][v8] - 1
        for v10 in range(v2):
            v11 = (v7 + v8) % 3
            v6[v11][v10] += v3[v9][v10]
v12 = 1000 * 500 * 500 * 10
for v13 in range(v2):
    for v14 in range(v2):
        for v15 in range(v2):
            if v13 != v14 != v15 != v13:
                v12 = min(v12, v6[0][v13] + v6[1][v14] + v6[2][v15])
print(v12)
