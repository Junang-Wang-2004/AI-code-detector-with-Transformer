v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = max((a for v6, v4 in v3))
v7 = [10 ** 18 for v4 in range(v1 + v5)]
v7[0] = 0
for v8 in range(1, v1 + v5):
    v7[v8] = min((v7[v8 - v6] + b for v6, v9 in v3))
print(min(v7[v1:]))
