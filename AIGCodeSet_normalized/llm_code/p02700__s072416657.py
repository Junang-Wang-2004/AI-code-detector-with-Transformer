v1, v2, v3, v4 = map(int, input().split())
if v1 - v4 * ((v3 + v2 - 1) // v2) > 0:
    print('Yes')
else:
    print('No')
