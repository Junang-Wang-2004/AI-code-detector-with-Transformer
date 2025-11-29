v1, v2, v3 = map(int, input().split())
v4 = [[] for v5 in range(v1)]
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v6 -= 1
    v7 -= 1
    v4[v6].append([v7, v8])
    v4[v7].append([v6, v8])
v9 = int(input())
v10 = []
for v5 in range(v9):
    v11, v12 = map(lambda x: int(x) - 1, input().split())
    v10.append([v11, v12])
v13 = [[-1] * v1 for v5 in range(v1)]
v14 = [0] * v1
for v5 in range(v1):
    v13[v5][v5] = 0

def f1(a1, a2):
    v14[a2] = 1
    for v1, v2 in v4[a2]:
        if v1 != a1:
            f1(a2, v1)
    for v1, v2 in v4[a2]:
        for v3 in range(v1):
            if v13[v1][v3] != -1:
                if v13[a2][v3] == -1:
                    v13[a2][v3] = v13[v1][v3] + v2
                    v13[v3][a2] = v13[v1][v3] + v2
                else:
                    v13[a2][v3] = min(v13[v1][v3] + v2, v13[a2][v3])
                    v13[v3][a2] = min(v13[v1][v3] + v2, v13[a2][v3])
f1(-1, 0)
for v5 in range(v9):
    v15 = v13[v10[v5][0]][v10[v5][1]]
    print(-1 if v15 < 0 else int((v15 - 0.1) // v3))
