def f1(a1):
    v1 = a1
    for v2 in range(len(v1)):
        for v3 in range(len(v1)):
            for v4 in range(len(v1)):
                v1[v3][v4] = min(v1[v3][v4], v1[v3][v2] + v1[v2][v4])
    return v1
v1, v2, v3 = map(int, input().split())
v4 = [v1 * [10 ** 10] for v5 in range(v1)]
for v6 in range(v1):
    v4[v6][v6] = 0
for v5 in range(v2):
    v7, v8, v9 = map(int, input().split())
    v7 -= 1
    v8 -= 1
    v4[v7][v8] = v4[v8][v7] = v9
v4 = f1(v4)
v10 = [v1 * [10 ** 10] for v5 in range(v1)]
for v6 in range(v1):
    v10[v6][v6] = 0
    for v11 in range(v1):
        if v4[v6][v11] <= v3:
            v10[v6][v11] = 1
v10 = f1(v10)
v12 = int(input())
for v5 in range(v12):
    v13, v14 = map(int, input().split())
    v13 -= 1
    v14 -= 1
    v15 = v10[v13][v14]
    if v15 == 10 ** 10:
        print(-1)
    else:
        print(v15 - 1)
