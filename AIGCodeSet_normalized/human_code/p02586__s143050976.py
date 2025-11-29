v1, v2, v3 = list(map(int, input().split()))
import copy
v4 = [[[0] * 4 for v5 in range(v2)] for v5 in range(2)]
v6 = [[0] * v2 for v5 in range(v1)]
for v5 in range(v3):
    v7, v8, v9 = list(map(int, input().split()))
    v7 -= 1
    v8 -= 1
    v6[v7][v8] = v9
for v10 in range(v1):
    for v11 in range(v2):
        v12 = 1
        v13 = v6[v10][v11]
        v14 = max(v4[v12 - 1][v11][0], v4[v12 - 1][v11][1], v4[v12 - 1][v11][2], v4[v12 - 1][v11][3], 0)
        v4[v12][v11][3] = max(v4[v12][v11 - 1][3], v4[v12][v11 - 1][2] + v13)
        v4[v12][v11][2] = max(v4[v12][v11 - 1][2], v4[v12][v11 - 1][1] + v13)
        v4[v12][v11][1] = max(v4[v12][v11 - 1][1], v4[v12][v11 - 1][0] + v13, v14 + v13)
        v4[v12][v11][0] = v14
    v4[0] = v4[1]
    v4[1] = [[0] * 4 for v5 in range(v2)]
v15 = 0
for v3 in range(4):
    v15 = max(v15, v4[0][v2 - 1][v3])
print(v15)
