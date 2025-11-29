v1 = input()
v2 = input()
v3 = list(v1)
v4 = list(v2)
v5 = 0
for v6 in range(len(v3)):
    if v3[v6] == v4[-v6 - 1]:
        v5 += 1
if v5 == 3:
    print('YES')
else:
    print('NO')
