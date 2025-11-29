v1 = int(input())
v2 = [int(i) for v3 in input().split(' ')]
v4 = []
v4.append(v2[0])
for v3 in v2:
    if v3 != v4[0] and len(v4) == 1:
        v4.append(v3)
    if v3 != v4[0] and v3 != v4[1]:
        v4.append(v3)
        break
if len(v4) == 1:
    if v4[0] == 0:
        print('Yes')
        exit(0)
    else:
        print('No')
        exit(0)
if len(v4) == 3:
    if v2.count(v4[0]) != v2.count(v4[1]):
        print('No')
        exit(0)
    if v2.count(v4[0]) != v2.count(v4[2]):
        print('No')
        exit(0)
    if len(v2) != v2.count(v4[0]) + v2.count(v4[1]) + v2.count(v4[2]):
        print('No')
        exit(0)
    if v4[0] ^ v4[1] == v4[2]:
        print('Yes')
        exit(0)
    elif v4[0] ^ v4[2] == v4[1]:
        print('Yes')
        exit(0)
    elif v4[1] ^ v4[2] == v4[0]:
        print('Yes')
        exit(0)
    else:
        print('No')
else:
    if len(v2) != v2.count(v4[0]) + v2.count(v4[1]):
        print('No')
        exit(0)
    if v4[0] == 0 or v4[1] == 0:
        if v4[0] == 0:
            if v2.count(v4[1]) != 2 * v2.count(v4[0]):
                print('No')
                exit(0)
        elif v2.count(v4[0]) != 2 * v2.count(v4[1]):
            print('No')
            exit(0)
        print('Yes')
        exit(0)
    else:
        print('No')
        exit(0)
