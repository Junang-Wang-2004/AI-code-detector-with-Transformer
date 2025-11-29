import itertools
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = 0
for v6, v7, v8 in itertools.product([-1, 1], repeat=3):
    v9 = [v6 * x + v7 * y + v8 * z for v10, v11, v12 in v3]
    v9.sort(reverse=True)
    v5 = max(v5, sum(v9[:v2]))
print(v5)
