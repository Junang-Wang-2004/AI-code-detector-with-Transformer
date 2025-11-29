v1, v2, v3 = map(int, input().split())
v4 = [0] * (v2 - 1)
v5 = 0
v6 = 10 ** 9 + 7
if v2 == 1:
    print(1)
    exit()
for v7 in range(2 ** (v2 - 1), 2 ** v2):
    v8 = bin(v7)[3:]
    v9 = True
    for v10 in range(v2 - 2):
        if v8[v10] == '1' and v8[v10 + 1] == '1':
            v9 = False
    if v9:
        v5 += 1
        for v10 in range(v2 - 1):
            v4[v10] += int(v8[v10])
v11 = [[0] * v2 for v7 in range(v1 + 1)]
v11[0][0] = 1
for v7 in range(v1):
    for v10 in range(v2):
        if v10 == 0:
            v11[v7 + 1][v10] = (v11[v7][v10] * (v5 - v4[0]) + v11[v7][v10 + 1] * v4[0]) % v6
        elif v10 == v2 - 1:
            v11[v7 + 1][v10] = (v11[v7][v10 - 1] * v4[v10 - 1] + v11[v7][v10] * (v5 - v4[v10 - 1])) % v6
        else:
            v11[v7 + 1][v10] = (v11[v7][v10 - 1] * v4[v10 - 1] + v11[v7][v10] * (v5 - v4[v10] - v4[v10 - 1]) + v11[v7][v10 + 1] * v4[v10]) % v6
print(v11[-1][v3 - 1])
