v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
for v4 in range(v2):
    v5 = [0] * (v1 + 1)
    for v6 in range(v1):
        v7 = max(1, v6 - v3[v6])
        v8 = min(v1 + 1, v6 + v3[v6] + 1)
        for v9 in range(v7, v8):
            v5[v9] += 1
    v3 = v5[1:]
print(*v3)
