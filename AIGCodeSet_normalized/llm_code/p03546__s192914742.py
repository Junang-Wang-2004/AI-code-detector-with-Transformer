import copy
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(10)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
v6 = copy.deepcopy(v3)
for v7 in range(10):
    for v8 in range(10):
        for v9 in range(10):
            v6[v8][v9] = min(v6[v8][v9], v6[v8][v7] + v6[v7][v9])
v10 = 0
for v8 in range(v1):
    for v9 in range(v2):
        if v5[v8][v9] != -1 and v5[v8][v9] != 1:
            v10 += v6[v5[v8][v9]][1]
print(v10)
