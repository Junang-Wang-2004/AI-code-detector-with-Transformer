v1 = input()
v2 = int(input())
v3 = len(v1)
v4 = v1 + v1
v5 = len(v4)
v6 = v4 + v1
v7 = len(v6)
v8 = 1
v9 = 0
v10 = 1
v11 = 0
v12 = 1
v13 = 0
for v14 in range(v3 - 1):
    if v1[v14] == v1[v14 + 1]:
        v8 += 1
    else:
        v9 += v8 // 2
        v8 = 1
v9 += v8 // 2
for v14 in range(v5 - 1):
    if v4[v14] == v4[v14 + 1]:
        v10 += 1
    else:
        v11 += v10 // 2
        v10 = 1
v11 += v10 // 2
for v14 in range(v7 - 1):
    if v6[v14] == v6[v14 + 1]:
        v12 += 1
    else:
        v13 += v12 // 2
        v12 = 1
v13 += v12 // 2
if v3 == 1:
    if v2 % 2 == 0:
        print(v2 // 2)
    else:
        print((v2 - 1) // 2)
elif v13 - v11 != v11 - v9:
    print((v13 - v11) * ((v2 + 1) // 2) + (v11 - v9) * (v2 // 2))
else:
    print((v13 - v11) * (v2 - 1) + v9)
