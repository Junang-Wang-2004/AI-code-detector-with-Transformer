v1 = input()
v2 = input()
v3 = {}
v4 = []
for v5 in range(len(v1)):
    if v1[v5] not in v3:
        v3[v1[v5]] = v5
    v4.append(v3[v1[v5]])
v6 = {}
v7 = []
for v5 in range(len(v2)):
    if v2[v5] not in v6:
        v6[v2[v5]] = v5
    v7.append(v6[v2[v5]])
if v4 == v7:
    print('Yes')
else:
    print('No')
