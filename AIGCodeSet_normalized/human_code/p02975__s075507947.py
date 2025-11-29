v1 = int(input())
v2 = [int(j) for v3 in input().split()]
import collections
v4 = collections.Counter(v2)
v5 = v4.most_common()
v6 = []
for v7, v3 in v5:
    v6.append(v7)
if sum(v6) == 0:
    print('Yes')
    exit()
if 0 in v6:
    if len(v5) == 2:
        for v7, v3 in v5:
            if v7 == 0:
                v8 = v3
            else:
                v9 = v3
        if 2 * v8 == v9:
            print('Yes')
            exit()
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()
v10 = v5[0][1]
v11 = []
if len(v5) == 3:
    for v7, v3 in v5:
        if v3 == v10:
            v11.append(v7)
        else:
            print('No')
            exit()
else:
    print('No')
    exit()
if v11[0] ^ v11[1] == v11[2] and v11[0] ^ v11[2] == v11[1] and (v11[2] ^ v11[1] == v11[0]):
    print('Yes')
else:
    print('No')
