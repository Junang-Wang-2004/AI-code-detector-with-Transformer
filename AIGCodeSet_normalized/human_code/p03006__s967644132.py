v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = []
for v3 in range(v1):
    v5, v6 = (v2[v3][0], v2[v3][1])
    for v7 in range(v1 - v3 - 1):
        v8 = v3 + v7 + 1
        v9, v10 = (v2[v8][0], v2[v8][1])
        v11 = v9 - v5
        v12 = v10 - v6
        if v11 <= 0:
            if v11 == 0:
                if v12 < 0:
                    v12 = -v12
            else:
                v11 = -v11
                v12 = -v12
        v4.append([v11, v12])
v13 = []
v14 = []
if v1 == 1:
    v13.append([0, 0])
    v14.append(1)
for v15 in v4:
    if v15 == [0, 0]:
        if [0, 0] not in v13:
            v13.append([0, 0])
            v14.append(1)
    elif v15 in v13:
        v14[v13.index(v15)] += 1
    else:
        v13.append(v15)
        v14.append(1)
v16 = max(v14)
if v1 == 1:
    print(1)
else:
    print(v1 - v16)
