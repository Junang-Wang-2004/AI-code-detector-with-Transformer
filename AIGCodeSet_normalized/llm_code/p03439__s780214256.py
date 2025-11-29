v1 = int(input())
for v2 in range(20):
    if v2 == 0:
        v3 = 0
        v4 = v1 - 1
        v5 = 0
        print(v5)
    else:
        v5 = (v3 + v4) // 2
        print(v5)
    v6 = input()
    v7 = v6[0]
    if v7 == 'V':
        exit()
    elif v2 == 0:
        v8 = v7
    elif v8 == v7:
        v3 = v5
    elif v5 % 2 == 1:
        print(v5 - 1)
        v6 = input()
        v7 = v6[0]
        if v7 == 'V':
            exit()
        else:
            print('E')
            exit()
    else:
        v8 = v7
        v4 = v5
print('End')
