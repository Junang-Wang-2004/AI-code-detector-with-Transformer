v1 = input()
v2 = int(input())
v3 = sorted(list(set(v1)))
v4 = 0
v5 = 0
for v6 in v3:
    v5 = v4
    v7 = [i for v8, v9 in enumerate(v1) if v9 == v6]
    v10 = []
    for v11 in v7:
        for v12 in range(v11 + 1, len(v1) + 1):
            v10.append(v1[v11:v12])
    v4 += len(v1)
    if v2 - 1 < v4:
        v13 = list(set(v10))
        v14 = sorted(v13)
        print(v14[v2 - v5 - 1])
        exit()
