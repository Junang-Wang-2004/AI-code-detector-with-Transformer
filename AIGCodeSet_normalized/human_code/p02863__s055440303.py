v1, v2 = map(int, input().split())
v3 = [0] * v1
v4 = [0] * v1
v5 = [[0 for v6 in range(v2 + 1)] for v7 in range(v1 + 1)]
v8 = [[0 for v6 in range(v2 + 1)] for v7 in range(v1 + 1)]
for v6 in range(v1):
    v4[v6], v3[v6] = map(int, input().split())
for v6 in range(v1):
    for v7 in range(v2 + 1):
        if v7 >= v4[v6]:
            if v8[v6 + 1][v7] < v8[v6][v7 - v4[v6]] + v3[v6]:
                v8[v6 + 1][v7] = v8[v6][v7 - v4[v6]] + v3[v6]
                v5[v6 + 1][v7] = v7 - v4[v6]
        if v8[v6 + 1][v7] < v8[v6][v7]:
            v8[v6 + 1][v7] = v8[v6][v7]
            v5[v6 + 1][v7] = v7
v9 = v8[-1][-1]
v10 = set()
v11 = v2 - 1
v6 = v1 - 1
while v6 >= 0:
    if v5[v6 + 1][v11] == v11 - v4[v6]:
        v10.add(v6)
    v11 = v5[v6 + 1][v11]
    v6 -= 1
v12 = 0
for v6 in range(v1):
    if v6 not in v10:
        v12 = max(v3[v6], v12)
print(max(v9, v8[-1][-2] + v12))
