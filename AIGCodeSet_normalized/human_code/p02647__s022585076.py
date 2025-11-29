v1, v2 = map(int, input().split())
v3 = [int(x) for v4 in input().split()]
v2 = min(v2, 41)
for v5 in range(v2):
    v6 = [0 for v5 in range(v1)]
    for v7 in range(v1):
        v8 = max(0, v7 - v3[v7])
        v9 = min(v1 - 1, v7 + v3[v7])
        v6[v8] += 1
        if v9 + 1 < v1:
            v6[v9 + 1] -= 1
    for v7 in range(1, v1):
        v6[v7] += v6[v7 - 1]
    v3 = v6
for v7 in range(v1):
    v3[v7] = str(v3[v7])
print(' '.join(v3))
