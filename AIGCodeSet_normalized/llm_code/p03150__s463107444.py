v1 = list(input())
v2 = list('keyence')
v3 = -1
for v4, v5 in enumerate(v2):
    v6 = v1.index(v5)
    if v3 < v6:
        v3 = v6
    else:
        print('NO')
        exit()
print('YES')
