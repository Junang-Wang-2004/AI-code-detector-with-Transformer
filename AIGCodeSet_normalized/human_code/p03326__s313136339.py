v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = 0
for v4 in range(8):
    v6 = []
    for v7 in range(v1):
        v8 = 0
        for v9 in range(3):
            if v4 >> v9 & 1:
                v8 += v3[v7][v9]
            else:
                v8 -= v3[v7][v9]
        v6.append(v8)
    v6.sort()
    v5 = max(v5, sum(v6[v1 - v2:]))
print(v5)
