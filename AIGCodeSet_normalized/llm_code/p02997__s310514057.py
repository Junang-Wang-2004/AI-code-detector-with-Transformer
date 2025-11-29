v1, v2 = map(int, input().split())
if v2 > (v1 - 1) * (v1 - 2) / 2:
    print('-1')
else:
    print(int(v1 * (v1 - 1) / 2 - v2))
    for v3 in range(v1 - 1):
        print('1', v3 + 2)
    v4 = (v1 - 2) * (v1 - 1) / 2 - v2
    v5 = 2
    for v6 in range(v1 - 1):
        for v7 in range(v1 - v6 - 2):
            print(2 + v6, 3 + v6 + v7)
            v4 = v4 - 1
            if v4 == 0:
                break
        if v4 == 0:
            break
