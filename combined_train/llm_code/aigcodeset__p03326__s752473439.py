v1, v2 = map(int, input().split())
v3 = []
v4 = []
v5 = []
for v6 in range(v1):
    v7, v8, v9 = map(int, input().split())
    v3.append(v7)
    v4.append(v8)
    v5.append(v9)
v10 = 0
v11 = 0
v12 = 0
for v6 in range(v2):
    v13 = []
    for v14 in range(v1 - v6):
        v15 = v10 + v3[v14]
        v16 = v11 + v4[v14]
        v17 = v12 + v5[v14]
        v13.append(abs(v15) + abs(v16) + abs(v17))
    print(v13)
    v18 = v13.index(max(v13))
    v10 = v10 + v3[v18]
    v11 = v11 + v4[v18]
    v12 = v12 + v5[v18]
    del v3[v18]
    del v4[v18]
    del v5[v18]
    v19 = abs(v10) + abs(v11) + abs(v12)
print(v19)
