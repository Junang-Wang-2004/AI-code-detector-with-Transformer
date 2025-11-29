import collections
v1, v2 = map(int, input().split())
v3 = [[0] * v2] * v1
for v4 in range(v1):
    v3[v4] = list(input())
if v1 == 1 and v2 == 1:
    print('Yes')
elif v1 == 1 or v2 == 1:
    v5 = []
    v6 = 0
    for v4 in range(v1):
        for v7 in range(v2):
            if v3[v4][v7] in v5:
                v6 += 1
                v5.remove(v3[v4][v7])
            else:
                v5.append(v3[v4][v7])
    if v1 == 1 and v2 % 2 == 0:
        if v6 == v2 // 2:
            print('Yes')
        else:
            print('No')
    elif v1 == 1 and v2 % 2 == 1:
        if v6 == v2 // 2:
            print('Yes')
        else:
            print('No')
    elif v2 == 1 and v1 % 2 == 0:
        if v6 == v1 // 2:
            print('Yes')
        else:
            print('No')
    elif v2 == 1 and v1 % 2 == 1:
        if v6 == v1 // 2:
            print('Yes')
        else:
            print('No')
else:
    v8 = [y for v9 in v3 for v10 in v9]
    v11 = collections.Counter(v8)
    if v1 % 2 == 0 and v2 % 2 == 0:
        v12 = 0
        for v13, v14 in v11.items():
            if v14 % 4 != 0:
                v12 = 1
        if v12 == 0:
            print('Yes')
        else:
            v15 = list(set(v8))
            if len(v15) == 1:
                print('Yes')
            else:
                print('No')
    elif v1 % 2 == 1 and v2 % 2 == 1:
        v16 = 0
        v17 = 0
        v18 = 0
        for v13, v14 in v11.items():
            if v14 % 4 != 0:
                if v14 % 2 == 0:
                    v17 += 1
                elif v14 % 2 == 1:
                    v18 += 1
                else:
                    v16 = 1
        if v16 == 0 and v17 == 2 and (v18 == 1) or (v16 == 0 and v17 == 0 and (v18 == 1)) or (v16 == 0 and v17 == 3 and (v18 == 1)) or (v16 == 0 and v17 == 1 and (v18 == 1)):
            print('Yes')
        else:
            v15 = list(set(v8))
            if len(v15) == 1:
                print('Yes')
            else:
                print('No')
    else:
        v16 = 0
        v17 = 0
        for v13, v14 in v11.items():
            if v14 % 4 != 0:
                if v14 % 4 == 2:
                    v17 += 1
                else:
                    v16 = 1
        if v1 % 2 == 1:
            v9 = v2 // 2
        elif v2 % 2 == 1:
            v9 = v1 // 2
        if v16 == 0 and v17 == v9:
            print('Yes')
        else:
            v15 = list(set(v8))
            if len(v15) == 1:
                print('Yes')
            else:
                print('No')
