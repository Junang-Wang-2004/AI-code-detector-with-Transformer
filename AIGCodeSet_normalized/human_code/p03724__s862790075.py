v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v5 -= 1
    v6 -= 1
    v3[v5] = (v3[v5] + 1) % 2
    v3[v6] = (v3[v6] + 1) % 2
if 1 in v3:
    print('NO')
else:
    print('YES')
