v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = [0] * (v1 + 1)
v9 = [0] * (v1 + 1)
v10 = [0] * (v1 + 1)
v11 = [0] * (v1 + 1)
v12 = 0
v13 = 0
for v14 in range(v1):
    v12 += v4[v14]
    v8[v14 + 1] = v12 - v3[v14]
    v9[v14 + 1] = max(v9[v14], v8[v14 + 1])
    v13 += v4[-v14 - 1]
    v10[v14 + 1] = v13 - (v2 - v3[-v14 - 1])
    v11[v14 + 1] = max(v11[v14], v10[v14 + 1])
v3 = [0] + v3
v4 = [0] + v4
v15 = max(0, v9[-1], v11[-1])
for v14 in range(1, v1 + 1):
    v15 = max(v15, v8[v14] + v11[v1 - v14] - v3[v14], v10[v14] + v9[v1 - v14] - (v2 - v3[v1 - v14 + 1]))
print(v15)
