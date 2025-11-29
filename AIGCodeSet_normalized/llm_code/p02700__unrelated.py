v1, v2, v3, v4 = map(int, input().split())
while v1 > 0 and v3 > 0:
    v3 -= v2
    if v3 <= 0:
        print('Yes')
        break
    v1 -= v4
    if v1 <= 0:
        print('No')
        break
