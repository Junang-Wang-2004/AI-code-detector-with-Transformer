v1, v2 = (int(x) for v3 in input().split())
v4 = v2 // 10000
v5 = v2 // 5000
v6 = v2 // 1000
v7 = 0
for v8 in range(v4 + 1):
    if v7 == 1:
        break
    for v9 in range(v5 + 1):
        if v8 + v9 > v1:
            break
        v10 = v1 - v8 - v9
        if 10 * v8 + 5 * v9 + v10 == v2 // 1000 and v10 >= 0:
            v11 = v8
            v12 = v9
            v7 = 1
            break
if v7 == 1:
    print('{0} {1} {2}'.format(v11, v12, v10))
else:
    v11, v12, v10 = (-1, -1, -1)
    print('{0} {1} {2}'.format(v11, v12, v10))
