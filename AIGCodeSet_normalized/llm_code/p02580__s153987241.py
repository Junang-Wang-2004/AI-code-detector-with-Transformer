v1, v2, v3 = map(int, input().split())
v4 = [[0 for v5 in range(v2)] for v6 in range(v1)]
v7 = [0 for v5 in range(v1)]
v8 = [0 for v6 in range(v2)]
for v9 in range(v3):
    v5, v6 = map(int, input().split())
    v7[v5 - 1] += 1
    v8[v6 - 1] += 1
    v4[v5 - 1][v6 - 1] = 1
v10 = max(v7)
v11 = max(v8)
v12 = 0
for v13 in range(v1):
    if v7[v13] == v10:
        for v14 in range(v2):
            if v8[v14] == v11:
                if v4[v13][v14] == 0:
                    v12 = 1
if v12 == 1:
    print(v10 + v11)
else:
    print(v10 + v11 - 1)
