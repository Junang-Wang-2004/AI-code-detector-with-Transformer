v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v4 = v5 = 0
for v6 in range(v1):
    if v2[v6] % 4 == 0:
        v5 += 1
    elif v2[v6] % 2 == 0:
        v4 += 1
    else:
        v3 += 1
if v4 == 0:
    v5 += 1
if v3 <= v5:
    print('Yes')
else:
    print('No')
