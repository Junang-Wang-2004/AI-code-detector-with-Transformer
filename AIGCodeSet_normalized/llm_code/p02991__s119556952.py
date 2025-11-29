v1, v2 = map(int, input().split())
v3 = list(([] for v4 in range(v1 * 3)))
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v7 = (v5 - 1) * 3
    v8 = (v5 - 1) * 3 + 1
    v9 = (v5 - 1) * 3 + 2
    v10 = (v6 - 1) * 3
    v11 = (v6 - 1) * 3 + 1
    v12 = (v6 - 1) * 3 + 2
    v3[v7].append(v11)
    v3[v8].append(v12)
    v3[v9].append(v10)
v13, v14 = map(int, input().split())
v15 = (v13 - 1) * 3
v16 = (v14 - 1) * 3
v17 = []
v17.extend(v3[v15])
v18 = 0
v19 = [0] * len(v3)
v20 = [0] * len(v3)
v20[v15] = 0
while len(v17) > 0:
    v4 = v17.pop(0)
    v18 = v20[v4]
    if v19[v4] == 1:
        continue
    if v4 == v16:
        print(int(v18 // 3 + 1))
        exit()
    v17.extend(v3[v4])
    for v21 in v3[v4]:
        v20[v21] = v18 + 1
    v19[v4] = 1
print(-1)
