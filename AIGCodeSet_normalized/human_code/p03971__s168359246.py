v1, v2, v3 = map(int, input().split())
v4 = input()
for v5 in range(v1):
    if v4[v5] == 'a':
        if v2 + v3 > 0:
            print('Yes')
            v2 -= 1
        else:
            print('No')
    if v4[v5] == 'b':
        if v2 + v3 > 0 and v3 > 0:
            print('Yes')
            v3 -= 1
        else:
            print('No')
    if v4[v5] == 'c':
        print('No')
