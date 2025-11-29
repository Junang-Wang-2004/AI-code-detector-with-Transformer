v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v3.append(list(map(int, input().split())))
v5 = []
for v4 in range(v1):
    v5.append(list(map(int, input().split())))
v6 = [[0] * 3 for v7 in range(v2)]
for v4 in range(v1):
    for v8 in range(v1):
        for v9 in range(v2):
            v6[(v4 + v8) % 3][v9] += v3[v5[v4][v8] - 1][v9]
v10 = float('inf')
for v4 in range(v2):
    for v8 in range(v2):
        for v9 in range(v2):
            if v4 != v8 and v8 != v9 and (v9 != v4):
                v10 = min(v10, v6[0][v4] + v6[1][v8] + v6[2][v9])
print(v10)
