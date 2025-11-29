v1, v2 = map(int, input().split())
v3 = [[int(i) for v4 in input().split()] for v5 in range(v1)]
v6 = [0] * v1
v7 = [0] * (v1 + 1)
v8 = 0
v9 = 0
v10 = (0, 0)
for v4, (v11, v12) in enumerate(v3):
    v8 += v12
    if v8 - v11 > v10[0]:
        v9 = v4
        v10 = (v8 - v11, v11)
    v6[v4] = v10
    v7[v4 + 1] = v8
if v10[0] == 0:
    print(0)
    exit(1)
v13 = 0
for v4, (v14, v12) in enumerate(v3):
    v15, v16 = (0, 0) if v4 == 0 else v6[v4 - 1]
    v17 = v7[v1] - v7[v4] - (v2 - v14)
    v13 = max(v13, v17 + v15 - min(v2 - v14, v16))
v13 = max(v13, v6[v1 - 1][0])
print(v13)
