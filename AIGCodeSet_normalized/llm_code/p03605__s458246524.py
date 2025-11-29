v1 = list(map(int, input().split()))
if len(v1) == 2:
    if v1[0] == 9 or v1[1] == 9:
        print('Yes')
    else:
        print('No')
elif v1[0] == 9:
    print('Yes')
else:
    print('No')
