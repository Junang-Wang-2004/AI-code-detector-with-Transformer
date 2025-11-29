import itertools
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6, v7 = map(int, input().split())
    v3.append((v5, v6, v7))
v8 = 0
for v9 in itertools.combinations(v3, v2):
    v10 = sum((v5 for v5, v6, v7 in v9))
    v11 = sum((v6 for v5, v6, v7 in v9))
    v12 = sum((v7 for v5, v6, v7 in v9))
    v13 = abs(v10) + abs(v11) + abs(v12)
    v8 = max(v8, v13)
print(v8)
