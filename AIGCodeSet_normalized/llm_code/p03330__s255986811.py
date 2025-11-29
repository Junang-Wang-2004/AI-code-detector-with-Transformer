from itertools import product
v1, v2 = map(int, input().split())
v3 = [map(int, input().split()) for v4 in range(v2)]
v5 = [map(int, input().split()) for v4 in range(v1)]
v6 = {(i, j): cost for v7, v8 in enumerate(v3) for v9, v10 in enumerate(v8)}
v11 = [[] for v4 in range(3)]
for v7, v8 in enumerate(v5):
    for v9, v12 in enumerate(v8):
        v11[(v7 + v9) % 3].append(v12 - 1)
v13 = [[(v12, sum((v6[cellcolor, v12] for v14 in cells))) for v12 in range(v2)] for v15 in v11]
v16 = [xs[:3] for v17 in v13]
v18 = (a[1] + b[1] + v2[1] for v19, v20, v2 in product(*v16) if len(set((v19[0], v20[0], v2[0]))) == 3)
print(min(v18))
