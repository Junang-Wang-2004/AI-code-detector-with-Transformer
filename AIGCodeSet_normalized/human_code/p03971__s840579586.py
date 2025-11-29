v1, v2, v3 = map(int, input().split())
v4 = input()
v5 = 0
v6 = 0
for v7 in v4:
    if v7 == 'a':
        if v5 + v6 < v2 + v3:
            print('Yes')
            v5 += 1
        else:
            print('No')
    elif v7 == 'b':
        if v5 + v6 < v2 + v3 and v6 < v3:
            print('Yes')
            v6 += 1
        else:
            print('No')
    else:
        print('No')
