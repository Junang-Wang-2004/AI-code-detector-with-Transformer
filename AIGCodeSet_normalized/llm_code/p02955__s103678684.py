v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v5 = sum(v3)
v6 = set()
v7 = 1
while v7 * v7 <= v5:
    if v5 % v7 == 0:
        v6.add(v7)
        v6.add(v5 // v7)
    v7 += 1
v8 = 1
for v9 in v6:
    v10 = [v3[v4] for v4 in range(v1)]
    for v4 in range(v1):
        if v3[v4] % v9 == 0:
            continue
        v11 = v3[v4] // v9 * v9
        v12 = v11 + v9
        if abs(v11 - v3[v4]) <= abs(v12 - v3[v4]):
            v10[v4] = v11
        else:
            v10[v4] = v12
    v13 = sum(v10)
    if v13 != v5:
        v10[0] += v5 - v13
    v14 = sum([abs(v3[v4] - v10[v4]) for v4 in range(v1)])
    if v14 <= 2 * v2:
        v8 = max(v8, v9)
print(v8)
