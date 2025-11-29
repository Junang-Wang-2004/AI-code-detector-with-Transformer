v1, v2, v3 = map(int, input().strip().split(' '))
v4 = list(input().strip())
v5 = 0
v6 = 0
for v7 in v4:
    if v7 == 'a':
        if v6 < v2 + v3:
            print('Yes')
            v6 += 1
        else:
            print('No')
    elif v7 == 'b':
        if v6 < v2 + v3 and v5 < v3:
            print('Yes')
            v5 += 1
            v6 += 1
        else:
            print('No')
    else:
        print('No')
