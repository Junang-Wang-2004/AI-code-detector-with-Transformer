v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
v5 = 0
for v6 in v2:
    if v6 % 4 == 0:
        v3 += 1
    elif v6 % 2 == 0:
        v4 += 1
    else:
        v5 += 1
if v3 >= v5 + max(0, v4 - 1):
    print('Yes')
else:
    print('No')
