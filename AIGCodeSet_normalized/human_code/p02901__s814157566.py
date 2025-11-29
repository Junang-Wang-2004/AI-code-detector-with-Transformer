def f1(a1):
    v1 = 0
    for v2 in a1:
        v1 += 2 ** (v2 - 1)
    return v1
v1, v2 = map(int, input().split())
v3 = 2 ** v1
v4 = float('inf')
v5 = [v4 for v6 in range(v3)]
v5[0] = 0
for v6 in range(v2):
    v7, v8 = map(int, input().split())
    v9 = f1(list(map(int, input().split())))
    for v10 in range(v3):
        v5[v10 | v9] = min(v5[v10 | v9], v5[v10] + v7)
if v5[-1] == v4:
    print(-1)
else:
    print(v5[-1])
