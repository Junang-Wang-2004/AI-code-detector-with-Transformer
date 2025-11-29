v1 = int(input())
v2 = list(map(int, input().split()))
v3 = True
for v4 in v2:
    if v4 % 2 == 0:
        if v4 % 3 == 0:
            pass
        elif v4 % 5 == 0:
            pass
        else:
            v3 = False
            break
if v3:
    print('APPROVED')
else:
    print('DENIED')
