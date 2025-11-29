v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
for v5 in v2:
    if v5 % 4 == 0:
        v4 += 1
    elif v5 % 2 == 0:
        v3 += 1
if v4 >= (v1 + 1) // 2 or v3 == v1:
    print('Yes')
else:
    print('No')
