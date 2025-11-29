v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [0 for v4 in range(v1 + 2)]
v6 = v5[:]
for v7, v8 in v3:
    v5[v7] += 1
    v5[v8] -= 1
for v9 in range(1, v1):
    v6[v9] = v5[v9] + v6[v9 - 1]
    if v6[v9] & 1:
        print('NO')
        break
else:
    print('YES')
