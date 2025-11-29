v1 = int(input())
v2 = list(map(int, input().split()))
v3, v4 = (0, 0)
for v5 in v2:
    if v5 % 2 == 0:
        v3 += 1
        if v5 % 3 == 0 or v5 % 5 == 0:
            v4 += 1
if v3 == v4:
    print('APPROVED')
else:
    print('DENIED')
