v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5 - 1].append(v6 - 1)
v7, v8 = map(int, input().split())
v7 -= 1
v8 -= 1
v9 = float('inf')
v10 = [[v9] * v1 for v4 in range(3)]
v10[0][v7] = 0
v11 = [[v7, 0]]
while v11:
    v12, v13 = v11.pop()
    if v12 == v8 and v13 == 0:
        break
    v14 = (v13 + 1) % 3
    for v15 in v3[v12]:
        if v10[v14][v15] != v9:
            continue
        else:
            v10[v14][v15] = v10[v13][v12] + 1
            v11.append([v15, v14])
v16 = v10[0][v8]
if v16 == v9:
    print(-1)
else:
    print(v16 // 3)
