v1, v2, v3 = map(int, input().split())
v4 = [tuple(map(int, input().split())) for v5 in range(v3)]
v6 = [0] * 10
if v3 == 0:
    v6[0] = 999999996000000004
    v6 = map(str, v6)
    print('\n'.join(v6))
    exit(0)
v7 = [[0] * v2 for v5 in range(v1)]
for v8 in v4:
    v7[v8[0] - 1][v8[1] - 1] = 1
for v9 in range(v1 - 2):
    for v10 in range(v2 - 2):
        v11 = 0
        for v5 in range(3):
            for v12 in range(3):
                v11 += v7[v9 + v5][v10 + v12]
        v6[v11] += 1
for v5 in range(10):
    print(v6[v5])
