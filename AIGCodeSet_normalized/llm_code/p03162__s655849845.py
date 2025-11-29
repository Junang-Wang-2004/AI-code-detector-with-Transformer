v1 = int(input())
v2 = []
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split())
    v2.append(v6)
    v3.append(v7)
    v4.append(v8)
v9 = [[0, 0, 0] for v5 in range(v1)]
v9[0][0] = v2[0]
v9[0][1] = v3[0]
v9[0][2] = v4[0]
for v10 in range(1, v1):
    v9[v10][0] = max(v9[v10 - 1][1], v9[v10 - 1][2]) + v2[v10]
    v9[v10][1] = max(v9[v10 - 1][2], v9[v10 - 1][0]) + v3[v10]
    v9[v10][2] = max(v9[v10 - 1][0], v9[v10 - 1][1]) + v4[v10]
print(max(v9[-1]))
