v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
v4 = {}
v5 = {}
for v6 in v2:
    if v3 == 1:
        if v6 in v4:
            v4[v6] = v4[v6] + 1
        else:
            v4[v6] = 1
        v3 = 0
    else:
        if v6 in v5:
            v5[v6] = v5[v6] + 1
        else:
            v5[v6] = 1
        v3 = 1
v7 = max(v4, key=v4.get)
v8 = max(v5, key=v5.get)
if v7 == v8:
    v9 = max(v4.values())
    v10 = max(v5.values())
    v4.pop(v7)
    v5.pop(v8)
    if v4 == {}:
        v11 = 0
    else:
        v11 = max(v4.values())
    if v5 == {}:
        v12 = 0
    else:
        v12 = max(v5.values())
    v13 = min(v1 - v9 - v12, v1 - v10 - v11)
    print(v13)
else:
    v13 = v1 - max(v4.values()) - max(v5.values())
    print(v13)
