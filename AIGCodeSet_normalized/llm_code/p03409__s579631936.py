v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2.append((v4, v5))
v6 = []
for v3 in range(v1):
    v7, v8 = map(int, input().split())
    v6.append((v7, v8))
v9 = 0
for v10 in range(101):
    v11 = v10
    v12 = 100 - v10
    v13 = []
    for v4, v5 in v2:
        v13.append((v11 * v4 + v12 * v5, v4, v5))
    v13.sort()
    v14 = []
    for v7, v8 in v6:
        v14.append((v11 * v7 + v12 * v8, v7, v8))
    v14.sort()
    v15 = 0
    v16 = set()
    for v3 in range(v1):
        v17, v18, v19 = v13[v3]
        for v20 in range(v1):
            if v20 in v16:
                continue
            v21, v22, v23 = v14[v20]
            if v18 < v22 and v19 < v23:
                v16.add(v20)
                v15 += 1
                break
    v9 = max(v9, v15)
print(v9)
