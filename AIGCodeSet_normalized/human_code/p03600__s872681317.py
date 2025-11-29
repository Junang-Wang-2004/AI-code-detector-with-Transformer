import copy
v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(list(map(int, input().split())))
v4 = copy.deepcopy(v2)
for v5 in range(v1):
    v4[v5][v5] = 0
for v6 in range(v1):
    for v5 in range(v1):
        for v7 in range(v1):
            v4[v5][v7] = min(v4[v5][v7], v4[v5][v6] + v4[v6][v7])
v8 = 0
for v5 in range(v1):
    for v7 in range(v5 + 1, v1):
        if v4[v5][v7] < v2[v5][v7]:
            print(-1)
            exit(0)
for v5 in range(v1):
    for v7 in range(v5 + 1, v1):
        v9 = True
        for v6 in range(v1):
            if v5 == v6 or v7 == v6:
                continue
            if v4[v5][v7] == v4[v5][v6] + v4[v6][v7]:
                v9 = False
        if v9:
            v8 += v4[v5][v7]
print(int(v8))
