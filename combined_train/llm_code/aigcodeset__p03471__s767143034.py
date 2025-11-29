v1, v2 = map(int, input().split())
min = v1 * 1000
max = v1 * 10000
if v2 > max or v2 < min:
    print('-1 -1 -1')
else:
    v3 = v2 - 5000 * v1 // 10000
    v1 -= v3
    v2 -= v3 * 10000
    v4 = v2 % 5000 // 1000
    v2 -= v4 * 1000
    v1 -= v4
    v5 = False
    for v6 in range(v2 // 10000):
        if v5:
            break
        v7 = v2 - v6 * 10000
        for v8 in range(v7 // 5000):
            v9 = v7 - v8 * 5000
            v10 = v9 // 1000
            if v6 + v8 + v10 == v1:
                print(str(v6 + v3) + ' ' + str(v8) + ' ' + str(v10 + v4))
                v5 = True
                break
    if not v5:
        print('-1 -1 -1')
