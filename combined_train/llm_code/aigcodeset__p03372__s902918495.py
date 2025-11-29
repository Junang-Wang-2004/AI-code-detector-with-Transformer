v1, v2 = map(int, input().split())
v3, v4 = ([], [])
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8, v9 = ([v3[0]] + [0] * (v1 - 1), [0] * (v1 - 1) + [v2 - v3[v1 - 1]])
for v5 in range(1, v1):
    v8[v5] = v3[v5] - v3[v5 - 1]
for v5 in range(v1 - 1):
    v9[v1 - 2 - v5] = v3[v1 - 1 - v5] - v3[v1 - 2 - v5]
v10, v11 = ([], [])
v12 = 0
for v5 in range(v1):
    v12 = v12 - v8[v5] + v4[v5]
    v10.append(v12)
v12 = 0
for v5 in range(v1):
    v12 = v12 - v9[v1 - 1 - v5] + v4[v1 - 1 - v5]
    v11.append(v12)
v13, v14 = ([], [])
if v10[0] > v10[1]:
    v13.append(0)
for v5 in range(1, v1 - 1):
    if v10[v5 + 1] < v10[v5] and v10[v5 - 1] < v10[v5]:
        v13.append(v5)
if v10[v1 - 1] == max(v10):
    v13.append(v1 - 1)
if v11[0] > v11[1]:
    v14.append(0)
for v5 in range(1, v1 - 1):
    if v11[v5 + 1] < v11[v5] and v11[v5 - 1] < v11[v5]:
        v14.append(v5)
if v11[v1 - 1] == max(v11):
    v14.append(v1 - 1)
v15 = 0
for v5 in v13:
    v12 = v10[v5]
    v15 = max(v15, v12)
    v12 -= v3[v5]
    for v16 in v14:
        if v16 < v1 - 1 - v5:
            v12 += v11[v16]
            v15 = max(v15, v12)
for v5 in v14:
    v12 = v11[v5]
    v15 = max(v15, v12)
    v12 -= v2 - v3[v1 - 1 - v5]
    for v16 in v13:
        if v16 < v1 - 1 - v5:
            v12 += v10[v16]
            v15 = max(v15, v12)
print(v15)
