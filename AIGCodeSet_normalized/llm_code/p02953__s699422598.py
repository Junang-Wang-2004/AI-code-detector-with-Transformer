v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[0]
v4 = 0
for v5 in v2[1:]:
    if v3 > v5 + 1:
        v4 = 1
        break
    v3 = max(v3, v5)
if v4 == 1:
    print('No')
else:
    print('Yes')
