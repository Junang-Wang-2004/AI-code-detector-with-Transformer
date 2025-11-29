v1 = input()
v2, v3 = map(int, input().split())
if 'T' not in v1:
    print('Yes' if v2 == len(v1) and v3 == 0 else 'No')
    exit()
v4 = v1.split('T')
v2 -= len(v4[0])
v5 = []
v6 = []
for v7, v8 in enumerate(v4[1:]):
    if not v8:
        continue
    if v7 % 2 == 0:
        v5.append(len(v8))
    else:
        v6.append(len(v8))
if not v6:
    if v2 != 0:
        print('No')
        exit()
else:
    v9 = set([0])
    for v10 in v6:
        v11 = set()
        for v12 in v9:
            v11.add(v12 + v10)
            v11.add(v12 - v10)
        v9 = v11
    if v2 not in v9:
        print('No')
        exit()
if not v5:
    if v3 != 0:
        print('No')
        exit()
else:
    v13 = set([0])
    for v14 in v5:
        v11 = set()
        for v15 in v13:
            v11.add(v15 + v14)
            v11.add(v15 - v14)
        v13 = v11
    if v3 not in v13:
        print('No')
        exit()
print('Yes')
