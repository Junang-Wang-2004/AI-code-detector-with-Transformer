v1 = int(input())
v2 = [[0 for v3 in range(3)] for v3 in range(v1)]
for v4 in range(v1):
    v5, v6, v7 = map(int, input().split())
    v2[v4][0] = v5
    v2[v4][1] = v6
    v2[v4][2] = v7
v8 = [[-1 for v3 in range(3)] for v3 in range(v1 + 1)]
for v4 in range(1, v1 + 1):
    for v9 in range(3):
        for v10 in range(3):
            if v4 == 1:
                v8[v4][v9] = v2[v4 - 1][v9]
            elif v9 == v10:
                continue
            else:
                v8[v4][v9] = max(v8[v4][v9], v8[v4 - 1][v10] + v2[v4 - 1][v9])
print(max(v8[v1]))
