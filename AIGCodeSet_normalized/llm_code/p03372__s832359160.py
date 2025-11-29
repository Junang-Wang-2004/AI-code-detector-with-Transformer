v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = [0 for v5 in range(v1)]
v8[0] = v4[0] - v3[0]
v9 = [0 for v5 in range(v1)]
v9[0] = max(0, v8[0])
for v10 in range(1, v1):
    v8[v10] = v8[v10 - 1] + v4[v10] - v3[v10] + v3[v10 - 1]
    v9[v10] = max(v8[v10], v9[v10 - 1])
v11 = v9[-1]
v7 = 0
for v10 in range(1, v1):
    v7 += v4[-v10]
    v11 = max(v11, v7 - (v2 - v3[-v10]), v7 - 2 * (v2 - v3[-v10]) + v9[-v10 - 1])
v11 = max(v11, v7 + v4[0] - (v2 - v3[0]))
print(v11)
