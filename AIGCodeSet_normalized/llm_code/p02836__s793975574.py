def f1():
    v1 = {}
    v2 = {}
    v1 = input()
    v2 = v1[::-1]
    v3 = len(v1)
    if v1 == v2:
        return 0
    v4 = {}
    v4[0] = 0
    for v5, v6 in enumerate(v1):
        v4[v5 + 1] = v6
    v1 = dict(v4)
    v4 = {}
    v4[0] = 0
    for v5, v6 in enumerate(v2):
        v4[v5 + 1] = v6
    v2 = dict(v4)
    v7 = [[0 for v8 in range(v3 + 1)]] * (v3 + 1)
    for v5 in v1:
        for v9 in v2:
            if v5 == 0 or v9 == 0:
                v7[v5][v9] = 0
            elif v1[v5] == v2[v9]:
                v7[v5][v9] = v7[v5 - 1][v9 - 1] + 1
            else:
                v7[v5][v9] = max(v7[v5][v9 - 1], v7[v5 - 1][v9])
    return v3 - v7[-1][-1]
print(f1())
