v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2 * 2)]
v5 = {v4 + 1 for v4 in range(v1)}
for v4 in range(1, v1 + 1, 2):
    for v6 in v3[v4]:
        for v7 in v6:
            v5.discard(v7)
print(len(v5))
