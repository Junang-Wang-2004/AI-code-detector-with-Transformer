v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(min(v1, v2 + 1)):
    for v6 in range(min(v1 - v5 + 1, v2 - v5 + 1)):
        v7 = sorted(v3[:v5] + v3[v1 - v6:])[::-1]
        for v8 in range(v2 - v5 - v6):
            if v7 and v7[-1] < 0:
                v7.pop()
        v4 = max(v4, sum(v7))
print(v4)
