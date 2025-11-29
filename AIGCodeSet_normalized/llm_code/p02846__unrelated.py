v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5, v6 = map(int, input().split())
v7 = v3 * v1 + v4 * v2
v8 = v5 * v1 + v6 * v2
v9 = abs(v7 - v8)
if v9 == 0:
    print('infinity')
    exit()
v10 = (v3 * v1 + v4 * v2) / v9
v11 = int(v10 / (v1 + v2))
if v11 == 0 and v10 > 0:
    print('infinity')
else:
    print(v11)
