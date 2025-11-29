from collections import *
v1 = defaultdict(list)
v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) + [i] for v5 in range(v2)]
v1[0] = [0, []]
for v6, v7, v8 in v4:
    for v9, v10 in v1.items():
        if v9 + v6 <= v3:
            if len(v1[v9 + v6]) == 2:
                if v10[0] + v7 > v1[v9 + v6][0]:
                    v1[v9 + v6] = [v10[0] + v7, v10[1] + [v8]]
            else:
                v1[v9 + v6] = [v10[0] + v7, v10[1] + [v8]]
v11, v12 = v1[max(v1.keys())]
for v5 in v12[::-1]:
    del v4[v5]
print(v11 + max((v5[1] for v5 in v4)))
