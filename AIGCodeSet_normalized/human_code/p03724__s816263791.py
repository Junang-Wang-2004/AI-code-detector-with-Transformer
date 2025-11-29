from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = defaultdict(int)
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5] += 1
    v3[v6] += 1
for v7 in v3:
    if v3[v7] % 2 != 0:
        print('NO')
        exit()
else:
    print('YES')
