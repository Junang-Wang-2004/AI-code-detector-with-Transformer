v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5, v6 = map(int, input().split())
if v3 > v5 and v4 > v6:
    print(0)
    exit()
if v5 > v3 and v6 > v4:
    print(0)
    exit()
if v3 < v5 and v4 > v6:
    v3, v5 = (v5, v3)
    v4, v6 = (v6, v4)
v7 = abs(v3 - v5)
v8 = abs(v4 - v6)
v9 = v7 * v1
v10 = v8 * v2
v11 = v10 - v9
if v11 < 0:
    print(0)
    exit()
if v11 == 0:
    print('infinity')
    exit()
if v9 % v11 != 0:
    v12 = v9 // v11 * 2 + 1
else:
    v12 = (v9 // v11 - 1) * 2 + 2
print(v12)
