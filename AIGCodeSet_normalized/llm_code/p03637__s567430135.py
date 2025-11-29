v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
for v5 in v2:
    if v5 % 4 == 0:
        v3 += 1
    elif v5 % 2 == 0:
        v4 += 1
v6 = len(v2) - v3 - v4
if len(v2) == 1 and v2[0] == 2:
    print('No')
elif v6 - v3 <= 1:
    print('Yes')
else:
    print('No')
