v1, v2, v3 = (int(x) for v4 in input().split())
if v1 < v2 < v3 or v1 > v2 > v3:
    print('No')
elif v3 < v2 or v2 < v1:
    print('No')
else:
    print('Yes')
