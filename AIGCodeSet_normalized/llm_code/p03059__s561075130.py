v1, v2, v3 = input().split()
v4 = int(v1)
v5 = int(v2)
v6 = int(v3)
if v6 % v4 == 0:
    v7 = v6 / v4 * v5
    print(v7)
else:
    v8 = v6 - v6 % v4
    print(v8)
