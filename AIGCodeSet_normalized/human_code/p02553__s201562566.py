v1, v2, v3, v4 = map(int, input().split())
v5 = float('-inf')
v6 = [v1, v2]
v7 = [v3, v4]
for v8 in v6:
    for v9 in v7:
        v5 = max(v5, v8 * v9)
print(v5)
