import itertools
v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v3)]
v6 = [v5 for v5 in range(1, v2 + 1)]
v5 = list(itertools.combinations_with_replacement(v6, v1))
v7 = 0
for v8 in v5:
    v9 = 0
    for v10 in v4:
        if v8[v10[1] - 1] - v8[v10[0] - 1] == v10[2]:
            v9 += v10[3]
    v7 = max(v7, v9)
print(v7)
