def f1(a1, a2, a3):
    v1 = {}
    for v2, v3, v4 in a1:
        if v2 in v1:
            v1[v2].append(v3)
        else:
            v1[v2] = [v3]
    v5 = [a2]
    v6 = []
    while v5:
        v7 = v5.pop()
        if v7 in v6:
            continue
        if v7 == a3:
            return True
        v6.append(v7)
        for v8 in v1.get(v7, ()):
            if v8 in v6 or v8 in v5:
                continue
            v5.append(v8)
    return False
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v4.append((v6, v7, v8))
v9 = float('-Inf')
v10 = False
v11 = 1
v12 = v1
v13 = {}
for v14 in range(1, v1 + 1):
    v13[v14] = v9
v13[v11] = 0
v15 = {}
for v14 in range(v1 - 1):
    for v16, v17, v18 in v4:
        if v13[v16] + v18 - v3 > v13[v17]:
            v13[v17] = v13[v16] + v18 - v3
            v15[v17] = v16
v19 = []
v20 = v12
while v20 != v11:
    v19.append(v20)
    v20 = v15[v20]
v19.append(v11)
for v16, v17, v18 in v4:
    if v13[v16] + v18 - v3 > v13[v17] and f1(v4, v17, v12):
        v10 = True
        break
if v10:
    print(-1)
else:
    print(max(0, v13[v12]))
