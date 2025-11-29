v1, v2 = map(int, input().split())
v3 = {}
for v4 in range(v1):
    v5 = list(input())
    for v6 in v5:
        v3[v6] = v3.get(v6, 0) + 1
v7 = 0
v8 = 0
for v6 in v3.values():
    if v6 % 2 == 1:
        v7 += 1
    if v6 % 4 == 2:
        v8 += 1
if v7 > v1 % 2 * (v2 % 2):
    print('No')
elif v8 > v2 * (v1 % 2) // 2 + v1 * (v2 % 2) // 2:
    print('No')
else:
    print('Yes')
