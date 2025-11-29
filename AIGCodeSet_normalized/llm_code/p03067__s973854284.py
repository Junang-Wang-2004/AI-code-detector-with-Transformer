v1, v2, v3 = map(int, input().split())
if v1 < v2:
    if v1 < v3 < v2:
        print('Yes')
    else:
        print('No')
elif v2 < v1:
    if v2 < v3 < v1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
