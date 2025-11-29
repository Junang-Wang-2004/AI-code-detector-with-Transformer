v1, v2, *v3 = map(int, open(0).read().split())
v4 = 0
for v5 in range(v2 + 1):
    for v6 in range(min(v1 + 1, v5 + 1)):
        for v7 in range(v6 + 1):
            v8 = v1 - v6 + v7
            v9 = v3[:v7] + v3[v8:]
            v9.sort()
            v4 = max(v4, sum(v9) - sum([t for v10 in v9 if v10 < 0][:v5 - v6]))
print(v4)
