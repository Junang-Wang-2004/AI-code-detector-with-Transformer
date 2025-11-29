v1, v2, v3 = map(int, input().split())
if v1 == v2 + v3 or v2 == v1 + v3 or v3 == v1 + v2:
    print('Yes')
else:
    print('No')
