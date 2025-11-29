v1, v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v1):
    v7, *v8 = list(map(int, input().split()))
    v5.append(v7)
    v4.append(v8)
v9 = []
for v10 in range(2 ** v1):
    v11 = [0] * v2
    v12 = 0
    for v13 in range(v1):
        if v10 >> v13 & 1 == 1:
            for v14 in range(v2):
                v11[v14] += v4[v13][v14]
            v12 += v5[v13]
    if min(v11) >= v3:
        v9.append(v12)
print(min(v9) if len(v9) > 0 else -1)
