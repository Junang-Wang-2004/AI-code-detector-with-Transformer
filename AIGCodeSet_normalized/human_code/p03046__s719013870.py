v1, v2 = map(int, input().split())
if v2 >= 2 ** v1:
    print(-1)
    exit()
elif v1 == 0:
    print('0 0')
elif v1 == 1:
    if v2 == 0:
        print('0 0 1 1')
    else:
        print(-1)
else:
    v3 = [i for v4 in range(2 ** v1) if v4 != v2]
    v5 = v3[::-1]
    for v6 in v3:
        print(v6, end=' ')
    print(v2, end=' ')
    for v7 in v5:
        print(v7, end=' ')
    print(v2)
