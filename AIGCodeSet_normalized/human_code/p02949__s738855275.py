v1, v2, v3 = [int(i) for v4 in input().split()]
v5 = [[int(v4) for v4 in input().split()] for v6 in range(v2)]
for v4 in v5:
    v4[0] -= 1
    v4[1] -= 1
    v4[2] -= v3
v7 = [-10 ** 18] * v1
v8 = [False] * v1
v9 = [False] * v1
v7[0] = 0
v8[0] = True
v9[-1] = True
for v6 in range(v1):
    for v10, v11, v12 in v5:
        if v8[v10]:
            v7[v11] = max(v7[v11], v7[v10] + v12)
            v8[v11] = True
        if v9[v11]:
            v9[v10] = True
v13 = v7[:]
for v6 in range(1):
    for v10, v11, v12 in v5:
        if v8[v10]:
            v7[v11] = max(v7[v11], v7[v10] + v12)
            v8[v11] = True
        if v9[v11]:
            v9[v10] = True
v14 = v7[:]
v15 = False
for v4 in range(v1):
    if v8[v4] and v9[v4]:
        if v13[v4] != v14[v4]:
            v15 = True
if v15:
    print('-1')
else:
    print(max(v13[-1], 0))
