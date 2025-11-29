from collections import defaultdict
v1, v2, v3 = list(map(int, input().split()))
v4 = [0] * v1
v5 = [0] * v2
v6 = defaultdict(set)
for v7 in range(v3):
    v8, v9 = list(map(int, input().split()))
    v4[v8 - 1] += 1
    v5[v9 - 1] += 1
    v6[v8 - 1].add(v9 - 1)
v10 = max(v4)
v11 = max(v5)
v12 = [i for v13, v14 in enumerate(v4) if v14 == v10]
v15 = [v13 for v13, v14 in enumerate(v5) if v14 == v11]
for v16 in v12:
    for v17 in v15:
        if v17 in v6[v16]:
            print(v10 + v11)
            exit()
else:
    print(v10 + v11 - 1)
