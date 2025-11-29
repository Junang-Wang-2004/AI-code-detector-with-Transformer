v1, = [int(x) for v2 in input().split()]
v3 = [int(v2) for v2 in input().split()]
v4 = v3
v5 = [None for v6 in range(v1 + 1)]
v7 = [None for v6 in range(v1 + 1)]
v7[0] = 1
for v6 in range(1, v1 + 1):
    v7[v6] = 2 * v7[v6 - 1] - v4[v6]
v5[v1] = 0
v7[v1] = 0
if v5[v1] + v4[v1] > 2 ** v1:
    print(-1)
    exit()
for v6 in range(v1 - 1, -1, -1):
    v5[v6] = (v5[v6 + 1] + v4[v6 + 1] + 1) // 2
    if v5[v6] + v4[v6] > 2 ** v6:
        print(-1)
        exit()
    v7[v6] = min(v7[v6], v7[v6 + 1] + v4[v6 + 1])
    if v5[v6] > v7[v6]:
        assert False
        print(-1)
        exit()
v8 = 0
for v6 in range(v1 + 1):
    v8 += v7[v6] + v4[v6]
print(v8)
