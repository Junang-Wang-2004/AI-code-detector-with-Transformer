import copy
v1 = list(input())
v2 = int(input())
if len(v1) == 1:
    print(v2 // 2)
elif len(v1) == 2:
    if v1[0] == v1[1]:
        print(v2)
    else:
        print(0)
else:
    v3 = copy.copy(v1)
    v4 = 0
    for v5 in range(1, len(v1)):
        if v1[v5 - 1] == v1[v5]:
            v4 += 1
            v1[v5] = 'change'
    if v1[0] == v1[-1]:
        v4 += 1
        v3[0] = 'change'
        for v5 in range(1, len(v3)):
            if v3[v5 - 1] == v3[v5]:
                v4 += 1
                v3[v5] = 'change'
        print((v2 - 1) * v4 + v1.count('change'))
    else:
        print(v2 * v4)
