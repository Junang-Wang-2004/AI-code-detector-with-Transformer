v1, v2 = map(int, input().split())
v3 = v1 * 4
v4 = v1 * 2
v5 = False
for v6 in range(v4, v3, 2):
    if v6 == v2:
        v5 = True
        break
if v5:
    print('Yes')
else:
    print('No')
