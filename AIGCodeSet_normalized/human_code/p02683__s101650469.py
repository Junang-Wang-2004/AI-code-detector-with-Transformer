from itertools import product as pr
v1, v2, v3 = [int(i) for v4 in input().split()]
v5 = [[int(v4) for v4 in input().split()] for v6 in range(v1)]
v7 = list(pr([0, 1], repeat=v1))
v8 = [[sum([v5[v6][k] * v4[v6] for v6 in range(v1)]) for v9 in range(v2 + 1)] for v4 in v7]
v10 = [v4[0] for v4 in v8 if all([v4[v6] >= v3 for v6 in range(1, v2 + 1)])]
if len(v10) == 0:
    print(-1)
else:
    print(min(v10))
