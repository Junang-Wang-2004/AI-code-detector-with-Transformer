v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v2 + 1):
    for v6 in range(v2 + 1 - v5):
        if v5 + v6 > v1:
            continue
        v7 = v3[:v5] + v3[v1 - v6:]
        v7.sort()
        v8 = sum(v7)
        for v9 in range(min(v2 - v5 - v6, v5 + v6)):
            if v7[v9] < 0:
                v8 -= v7[v9]
        v4 = max(v4, v8)
print(v4)
