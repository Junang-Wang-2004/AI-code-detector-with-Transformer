v1 = int(input())
v2 = [int(x) for v3 in input().split()]
v4 = 0
for v5 in range(v1):
    if v2[v5] % 2 == 0:
        if v2[v5] % 3 != 0 and v2[v5] % 5 != 0:
            v4 = 1
if v4 == 1:
    print('DENIED')
else:
    print('APPROVED')
