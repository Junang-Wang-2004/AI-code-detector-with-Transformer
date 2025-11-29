v1, v2 = [int(i) for v3 in input().split()]
if v1 % 2 == 1:
    v4 = 1
    v5 = 2 * v2
    for v6 in range(v2):
        print(v4, v5)
        v4 += 1
        v5 -= 1
else:
    v4 = 1
    v7 = v1 - 1
    v8 = 0
    v9 = v1 // 2
    v10 = True
    while True:
        if v10 and v7 <= v9:
            v7 -= 1
            v10 = False
        v8 += 1
        print(v4, v4 + v7)
        v4 += 1
        v7 -= 2
        if v8 == v2:
            break
