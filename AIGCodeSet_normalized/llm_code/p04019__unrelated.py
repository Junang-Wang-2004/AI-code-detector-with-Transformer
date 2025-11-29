v1 = input()
v2 = len(v1)
v3 = 0
v4 = 0
v5 = 0
v6 = 0
for v7 in range(v2):
    if v1[v7] == 'N':
        v3 += 1
    elif v1[v7] == 'W':
        v4 += 1
    elif v1[v7] == 'S':
        v5 += 1
    else:
        v6 += 1
if v3 == v5 and v4 == v6:
    print('Yes')
else:
    print('No')
