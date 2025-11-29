import collections
v1, v2 = map(int, input().split())
v3 = [input() for v4 in [0] * v1]
v5 = [[-1] * v2 for v6 in [0] * v1]
v7 = 0
for v8 in range(v1):
    for v9 in range(v2):
        if v5[v8][v9] != -1:
            continue
        v5[v8][v9] = v7
        v10 = collections.deque()
        v10.append((v8, v9))
        while len(v10) > 0:
            v4, v11 = v10.popleft()
            v12 = v3[v4][v11]
            if v4 + 1 < v1 and v5[v4 + 1][v11] == -1 and (v12 != v3[v4 + 1][v11]):
                v5[v4 + 1][v11] = v7
                v10.append((v4 + 1, v11))
            if v4 - 1 >= 0 and v5[v4 - 1][v11] == -1 and (v12 != v3[v4 - 1][v11]):
                v5[v4 - 1][v11] = v7
                v10.append((v4 - 1, v11))
            if v11 + 1 < v2 and v5[v4][v11 + 1] == -1 and (v12 != v3[v4][v11 + 1]):
                v5[v4][v11 + 1] = v7
                v10.append((v4, v11 + 1))
            if v11 - 1 >= 0 and v5[v4][v11 - 1] == -1 and (v12 != v3[v4][v11 - 1]):
                v5[v4][v11 - 1] = v7
                v10.append((v4, v11 - 1))
        v7 += 1
v13 = {}
v14 = {}
for v4 in range(v1):
    for v11 in range(v2):
        v15 = v5[v4][v11]
        if v3[v4][v11] == '#':
            v13[v15] = v13.get(v15, 0) + 1
        else:
            v14[v15] = v14.get(v15, 0) + 1
v16 = 0
for v4 in range(v7):
    v16 += v13.get(v4, 0) * v14.get(v4, 0)
print(v16)
