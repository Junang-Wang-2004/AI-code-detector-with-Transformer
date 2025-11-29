v1, v2 = map(int, input().split())
v3 = {}
for v4 in range(26):
    v3[chr(v4 + 97)] = 0
for v4 in range(v1):
    v5 = input()
    for v6 in v5:
        v3[v6] += 1
if v1 == 1 and v2 == 1:
    print('Yes')
elif v1 == 1 or v2 == 1:
    v7 = 0
    for v4 in v3.values():
        if v4 % 2 == 1:
            v7 += 1
    if v7 != 1:
        print('No')
    else:
        print('Yes')
elif v1 % 2 == 0 and v2 % 2 == 0:
    for v4 in v3.values():
        if v4 % 4 != 0:
            print('No')
            exit()
    print('Yes')
elif v1 % 2 == 1 and v2 % 2 == 0:
    v7 = 0
    for v4 in v3.values():
        if v4 % 4 == 1 or v4 % 4 == 3:
            print('No')
            exit()
        if v4 % 4 == 2:
            v7 += 1
    if v7 > v2 // 2:
        print('No')
    else:
        print('Yes')
elif v1 % 2 == 0 and v2 % 2 == 1:
    v7 = 0
    for v4 in v3.values():
        if v4 % 4 == 1 or v4 % 4 == 3:
            print('No')
            exit()
        if v4 % 4 == 2:
            v7 += 1
    if v7 > v1 // 2:
        print('No')
    else:
        print('Yes')
else:
    v8 = 0
    v9 = 0
    v10 = 0
    for v4 in v3.values():
        if v4 % 4 == 1:
            v10 += 1
        elif v4 % 4 == 2:
            v9 += 1
        elif v4 % 4 == 3:
            v8 += 1
    v11 = 1 - v10
    if v10 + v8 != 1:
        print('No')
    elif v9 + v8 - v11 > (v1 - 1) // 2 + (v2 - 1) // 2:
        print('No')
    else:
        print('Yes')
