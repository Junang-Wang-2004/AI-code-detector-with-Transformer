v1, v2, v3 = map(int, input().split())
v4 = [[999999999999 if i != j else 0 for v5 in range(v1)] for v6 in range(v1)]
for v6 in range(v2):
    v7, v8, v9 = map(int, input().split())
    v7, v8 = (v7 - 1, v8 - 1)
    if v9 > v3:
        continue
    v4[v7][v8] = v9
    v4[v8][v7] = v9
for v10 in range(v1):
    for v6 in range(v1):
        for v5 in range(v1):
            if v4[v6][v5] > v4[v6][v10] + v4[v10][v5]:
                v4[v6][v5] = v4[v6][v10] + v4[v10][v5]
for v6 in range(v1):
    for v5 in range(v1):
        if v4[v6][v5] <= v3:
            v4[v6][v5] = 1
for v10 in range(v1):
    for v6 in range(v1):
        for v5 in range(v1):
            if v4[v6][v5] > v4[v6][v10] + v4[v10][v5]:
                v4[v6][v5] = v4[v6][v10] + v4[v10][v5]
for v6 in range(int(input())):
    v11, v12 = map(int, input().split())
    v11 -= 1
    v12 -= 1
    print(v4[v11][v12] - 1 if v4[v11][v12] - 1 < 99999999999 else -1)
