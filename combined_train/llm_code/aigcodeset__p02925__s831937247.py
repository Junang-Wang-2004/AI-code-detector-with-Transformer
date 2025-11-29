import os
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = v1 * (v1 - 1) // 2
id = [[-1 for v5 in range(v1)] for v5 in range(v1)]
v6 = [[] for v5 in range(v4)]

def f1(a1, a2):
    if a1 > a2:
        a2, a1 = (a1, a2)
    return id[a1][a2]
v7 = [False for v5 in range(v4)]
v8 = [False for v5 in range(v4)]
v9 = [-1 for v5 in range(v4)]

def f2(a1):
    if v7[a1]:
        if not v8[a1]:
            return -1
        else:
            return v9[a1]
    v7[a1] = True
    v9[a1] = 1
    for v1 in v6[a1]:
        v2 = f2(v1)
        if v2 == -1:
            return -1
        v9[a1] = max(v9[a1], v2 + 1)
    v8[a1] = True
    return v9[a1]
v10 = 0
for v3 in range(v1):
    for v11 in range(v1):
        if v3 < v11:
            id[v3][v11] = v10
            v10 += 1
for v3 in range(v1):
    for v11 in range(v1 - 1):
        v2[v3][v11] = f1(v3, v2[v3][v11] - 1)
    for v11 in range(v1 - 2):
        v6[v2[v3][v11 + 1]].append(v2[v3][v11])
v12 = 0
for v3 in range(v10):
    v13 = f2(v3)
    if v13 == -1:
        print(-1)
        os._exit(0)
    v12 = max(v12, v13)
print(v12)
