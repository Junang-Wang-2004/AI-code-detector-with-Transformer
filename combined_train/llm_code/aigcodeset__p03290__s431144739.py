v1, v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v3.append(list(map(int, input().split())))
v5 = [0 for v4 in range(v1)]
for v4 in range(v1):
    v5[v4] = (v4 + 1) * 100 * v3[v4][0] + v3[v4][1]
v6 = [[] for v4 in range(2 ** v1)]
for v4 in range(2 ** v1):
    for v7 in range(v1):
        v6[v4].append(v4 // 2 ** v7 % 2)
v8 = 10 ** 8
for v9 in v6:
    v10 = 0
    v11 = 0
    for v4 in range(len(v9)):
        if v9[v4] == 1:
            v10 += v5[v4]
            v11 += v3[v4][0]
    for v7 in range(v1):
        v12 = v11
        v13 = (v7 + 1) * 100 * v3[v7][0]
        v14 = v2 - v10
        if v14 < 0 or v9[v7] == 1:
            v12 = 10 ** 8
        elif v14 == 0:
            v12 = v11
        elif v14 > 0:
            if v14 <= v13:
                v12 += v14 // ((v7 + 1) * 100)
                if v14 % ((v7 + 1) * 100) > 0:
                    v12 += 1
            else:
                v12 = 10 ** 8
        if v12 < v8:
            v8 = v12
print(v8)
