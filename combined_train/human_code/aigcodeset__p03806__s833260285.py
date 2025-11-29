import copy
v1, v2, v3 = [int(n) for v4 in input().split()]
v5 = {(0, 0): 0}
for v6 in range(v1):
    v7, v8, v9 = [int(v4) for v4 in input().split()]
    v10 = copy.deepcopy(v5)
    for v11, v12 in v10.items():
        v13 = (v11[0] + v7, v11[1] + v8)
        if v13 in v5:
            if v5[v13] > v12 + v9:
                v5[v13] = v12 + v9
        else:
            v5[v13] = v12 + v9
v14 = 1000000
for v6 in range(1, 401):
    if (v2 * v6, v3 * v6) in v5:
        v14 = min(v5[v2 * v6, v3 * v6], v14)
if v14 == 1000000:
    print(-1)
else:
    print(v14)
