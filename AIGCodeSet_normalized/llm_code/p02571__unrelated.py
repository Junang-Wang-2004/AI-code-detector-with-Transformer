v1 = input()
v2 = input()
v3 = len(v1)
v4 = len(v2)
v5 = [[float('inf')] * (v4 + 1) for v6 in range(v3 + 1)]
for v7 in range(v3 + 1):
    v5[v7][0] = 0
for v7 in range(1, v3 + 1):
    for v8 in range(1, v4 + 1):
        if v1[v7 - 1] == v2[v8 - 1]:
            v5[v7][v8] = v5[v7 - 1][v8 - 1]
        else:
            v5[v7][v8] = min(v5[v7 - 1][v8], v5[v7][v8 - 1]) + 1
print(v5[v3][v4])
