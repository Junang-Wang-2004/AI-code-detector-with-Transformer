v1, v2, v3 = map(int, input().split())
v4 = input()
v2 += v3
v5 = 0
v6 = 0
for v7 in range(v1):
    if v4[v7] == 'a':
        if v5 < v2:
            print('Yes')
            v5 += 1
        else:
            print('No')
    elif v4[v7] == 'b':
        if v5 < v2 and v6 < v3:
            print('Yes')
            v5 += 1
            v6 += 1
        else:
            print('No')
    else:
        print('No')
