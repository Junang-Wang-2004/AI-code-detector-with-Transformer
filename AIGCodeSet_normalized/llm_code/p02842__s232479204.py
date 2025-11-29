v1 = int(input())
if 1 <= v1 and v1 <= 50000:
    v2 = False
    v3 = 0
    v4 = int(v1 / 1.08)
    v5 = int(v1 / 1.07)
    for v6 in range(v4, v5 + 1):
        v7 = int(v6 * 1.08)
        if v7 == v1:
            v2 = True
            break
    if v2:
        print(v6)
    else:
        print(':(')
else:
    print(':(')
