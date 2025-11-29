v1 = input()
v2 = 'keyence'
v3 = -1
for v4 in range(len(v1)):
    if not v1[v4] == v2[v4]:
        v3 = v4
        break
v5 = True
if v3 != -1:
    for v4 in range(1, len(v2) - v3 + 1):
        if not v1[-v4] == v2[-v4]:
            v5 = False
            break
if v5:
    print('YES')
else:
    print('NO')
