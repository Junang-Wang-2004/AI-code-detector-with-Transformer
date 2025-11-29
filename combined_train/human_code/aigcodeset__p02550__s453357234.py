v1, v2, v3 = map(int, input().split())
v4 = min(v1, v3)
v5 = set()
v6 = []
v7 = 0
for v8 in range(v4):
    if v2 in v5:
        break
    v5.add(v2)
    v6.append(v2)
    v7 += v2
    v2 = v2 * v2 % v3
if len(v6) >= v4:
    print(v7)
    exit()
v9 = v6.index(v2)
v10 = len(v6) - v9
v11 = (v1 - v9) % v10
v12 = (v1 - v9) // v10
v13 = sum(v6[:v9])
v14 = v7 - v13
v15 = sum(v6[v9:v9 + v11])
print(v13 + v14 * v12 + v15)
