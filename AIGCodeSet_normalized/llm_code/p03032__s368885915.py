v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(min(v2 + 1, v1 + 1)):
    for v6 in range(v5 + 1):
        v7 = v5 - v6
        v8 = v3[:v6] + v3[v1 - v7:]
        v8.sort()
        v9 = sum(v8)
        v10 = min(v2 - v5, len(v8))
        for v11 in range(v10):
            if v8[v11] < 0:
                v9 -= v8[v11]
            else:
                break
        v4 = max(v9, v4)
print(v4)
