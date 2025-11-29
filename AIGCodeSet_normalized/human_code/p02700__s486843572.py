v1, v2, v3, v4 = map(int, input().split())
while v1 > 0 and v3 > 0:
    v3 -= v2
    v1 -= v4
if v3 <= 0:
    print('Yes')
else:
    print('No')
