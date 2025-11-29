v1, v2, v3, v4 = map(int, input().split())
if abs(v1 - v2) % 2 == 1 and abs(v3 - v4) % 2 == 0:
    print('No')
else:
    print('Yes')
