v1, v2, v3, v4 = map(int, input().split())
v5 = 0
if v4 >= v1:
    v5 += v1
    v4 -= v1
else:
    v5 += v4
    print(v5)
    exit()
if v4 == 0:
    print(v5)
    exit()
if v4 >= v2:
    v4 -= v2
else:
    print(v5)
    exit()
if v4 == 0:
    print(v5)
    exit()
v5 -= v4
print(v5)
