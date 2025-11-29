v1, v2 = map(int, input().split())
v3 = []
v4 = []
v5 = {}
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v5[v7] = v5.get(v7, 0) + v8
v5 = sorted(v5.items(), key=lambda x: x[0])
v9 = 0
for v10, v11 in v5:
    v3.append(v10)
    v4.append(v9 + v11)
    v9 += v11
for v12 in range(len(v4)):
    if v2 <= v4[v12]:
        break
print(v3[v12])
