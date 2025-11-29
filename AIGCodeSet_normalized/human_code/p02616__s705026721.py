v1 = 10 ** 9 + 7
v2, v3, *v4 = map(int, open(0).read().split())
v5, v6 = ([], [])
for v7 in v4:
    if v7 < 0:
        v6 += [v7]
    else:
        v5 += [v7]
v8, v9 = (len(v5), len(v6))
v10 = 0
if v8:
    if v2 == v3:
        v10 = 1 - v9 % 2
    else:
        v10 = 1
else:
    v10 = 1 - v3 % 2
v11 = 1
if v10 < 1:
    v4.sort(key=lambda x: abs(x))
    for v7 in range(v3):
        v11 = v11 * v4[v7] % v1
else:
    v5.sort()
    v6.sort(reverse=1)
    if v3 % 2:
        v11 = v5.pop()
    v12 = []
    while len(v5) > 1:
        v12 += [v5.pop() * v5.pop()]
    while len(v6) > 1:
        v12 += [v6.pop() * v6.pop()]
    v12.sort(reverse=1)
    for v7 in range(v3 // 2):
        v11 = v11 * v12[v7] % v1
print(v11)
