v1 = input()
v2 = 0
v3 = 0
v4 = 0
v5 = 0
for v6 in range(len(v1)):
    if v1[v6] == 'N':
        v2 += 1
    elif v1[v6] == 'E':
        v3 += 1
    elif v1[v6] == 'W':
        v4 += 1
    else:
        v5 += 1
if v2 == v5 and v3 == v4:
    print('Yes')
else:
    print('No')
