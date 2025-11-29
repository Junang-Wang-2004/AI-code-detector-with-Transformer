v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5, v6 = map(int, input().split())
v7, v8, v9, v10 = (v1 * v3, v1 * v5, v2 * v4, v2 * v6)
if v7 + v9 == v8 + v10:
    print('infinity')
elif (v7 - v8) * (v9 - v10) > 0:
    print(0)
else:
    v11, v12 = (abs(v7 - v8), abs(v9 - v10))
    if (v11 + v12) % (v11 - v12) == 0:
        print((v11 + v12) // (v11 - v12))
    else:
        print((v11 + v12) // (v11 - v12) + 1)
