v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v3.append(list(map(int, input().split())))
v5 = [0] * 10 ** 5
for v4 in range(v2):
    for v6 in range(2):
        v5[v3[v4][v6] - 1] += 1
v7 = True
for v4 in range(10 ** 5):
    if v5[v4] % 2 != 0:
        v7 = False
        break
if v7:
    print('YES')
else:
    print('NO')
