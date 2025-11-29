v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 1
v5 = 1
v6 = []
v7 = 0
v8 = 0
v9 = 0
if v3[0] == 1:
    v9 = 1
elif v1 >= v2:
    for v10 in range(v2 - 1):
        v11 = v3[v4 - 1]
        v4 = v11
    v9 = v4
else:
    for v10 in range(v1):
        v11 = v3[v4 - 1]
        v4 = v11
        v12 = len(v6)
        for v13 in range(v12):
            if v4 == v6[v13]:
                v8 = v10 - v13 + 1
                v7 = 1
                v14 = v10 + 1
                break
        if v7 == 1:
            break
        else:
            v6.append(v4)
    if v8 == 1:
        v9 = v3[v14]
    else:
        v15 = v2 % v8
        v9 = v3[v14 + v15 - 1 - v8]
print(v9)
