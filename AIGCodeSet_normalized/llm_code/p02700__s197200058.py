v1, v2, v3, v4 = [int(x) for v5 in input().split()]
while v1 > 0 and v3 > 0:
    v3 -= v2
    v1 -= v2
if v1 <= 0:
    print('No')
else:
    print('Yes')
