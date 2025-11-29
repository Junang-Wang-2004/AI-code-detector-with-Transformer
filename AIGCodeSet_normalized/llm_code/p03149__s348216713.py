v1 = [int(_) for v2 in input().split()]
list = [1, 7, 9, 4]
v3 = True
for v4 in v1:
    if v4 in list:
        pass
    else:
        v3 = False
        break
if v3:
    print('YES')
else:
    print('NO')
