v1 = [int(x) for v2 in input().split()]
if v1[0] < v1[2] < v1[1] or v1[0] > v1[2] > v1[1]:
    print('Yes')
else:
    print('No')
