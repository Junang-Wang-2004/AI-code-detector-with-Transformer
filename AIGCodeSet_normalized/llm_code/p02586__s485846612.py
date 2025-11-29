import sys
v1 = [int(x) for v2 in sys.stdin.readline().split()]
v3 = 0
v4, v5, v6 = v1[v3:v3 + 3]
v3 += 3
v7 = [[] for v8 in range(v4 + 1)]
v9 = [0] * (v5 + 1)
for v8 in range(v6):
    v10, v11, v12 = v1[v3:v3 + 3]
    v3 += 3
    v7[v10].append([v11, v12])
for v13 in range(v4 + 1):
    v7[v13].sort()
v14 = 0
for v10 in range(1, v4 + 1):
    v15 = []
    v16, v17 = (0, 0)
    v18 = v7[v10]
    for v11, v12 in v18:
        v19 = v9[v11] + v12
        v20 = v16 + v12
        v21 = v17 + v12
        v22 = v19
        if v22 < v20:
            v22 = v20
        if v22 < v21:
            v22 = v21
        v15.append(v22)
        if v19 > v16:
            v16 = v19
        if v20 > v17:
            v17 = v20
        if v14 < v22:
            v14 = v22
    for v23 in range(len(v15)):
        if v9[v18[v23][0]] < v15[v23]:
            v9[v18[v23][0]] = v15[v23]
    for v23 in range(2, v5 + 1):
        if v9[v23] < v9[v23 - 1]:
            v9[v23] = v9[v23 - 1]
print(v14)
