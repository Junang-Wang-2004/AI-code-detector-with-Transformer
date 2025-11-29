v1, v2 = map(int, input().split())
for v3 in range(1, v1 - v3):
    v4 = 2 * v3 + 4 * (v1 - v3)
    if v4 == v2:
        print('Yes')
        break
    v4 = 2 * v3
    if v4 == v2:
        print('Yes')
        break
    else:
        print('No')
