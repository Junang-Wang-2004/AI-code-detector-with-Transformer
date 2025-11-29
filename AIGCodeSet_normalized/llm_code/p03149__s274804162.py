v1 = input().split()
v2 = 0
for v3 in v1:
    if int(v3) not in [1, 9, 7, 4]:
        v2 = 1
        break
if v2 == 0:
    print('YES')
else:
    print('NO')
