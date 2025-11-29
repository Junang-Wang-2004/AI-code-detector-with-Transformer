v1, v2, v3 = map(int, input().split())
if v1 < v3 and v3 < v2:
    print('Yes')
elif v2 < v3 and v3 < v1:
    print('Yes')
else:
    print('No')
