v1, v2, v3 = map(int, input().split())
v4 = input()
v5 = v2 + v3
for v6 in range(v1):
    if v5 == 0:
        print('No')
    elif v5 > 0 and v3 == 0 and (v4[v6] == 'b'):
        print('No')
    elif v4[v6] == 'a':
        print('Yes')
        v5 -= 1
    elif v4[v6] == 'b':
        print('Yes')
        v5 -= 1
        v3 -= 1
    else:
        print('No')
