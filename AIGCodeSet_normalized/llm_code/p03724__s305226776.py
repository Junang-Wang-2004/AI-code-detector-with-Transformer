v1, v2 = map(int, input().split())
v3 = [0] * v1
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v5 -= 1
    v6 -= 1
    v3[v5] += 1
    v3[v6] += 1
v7 = True
for v4 in range(v1):
    if v3[v4] % 2 != 0:
        v7 = False
        break
if v7:
    print('YES')
else:
    print('NO')
