v1 = list(map(lambda x: int(x), input().strip().split()))
v2 = v1[0]
v3 = v1[1]
v4 = []
for v5 in range(v2):
    v6 = list(map(lambda x: int(x), input().strip().split()))
    v4.append(v6)
v7 = 0
v8 = 0
v9 = []
for v5 in range(v2):
    if v5 % 2 == 0:
        for v10 in range(v3):
            if v4[v5][v10] % 2 == 0:
                continue
            if not v10 == v3 - 1:
                v4[v5][v10] = v4[v5][v10] - 1
                v4[v5][v10 + 1] = v4[v5][v10 + 1] + 1
                v9.append('{} {} {} {}'.format(v5 + 1, v10 + 1, v5 + 1, v10 + 2))
                v7 += 1
            elif v5 != v2 - 1:
                v4[v5][v10] = v4[v5][v10] - 1
                v4[v5 + 1][v10] = v4[v5 + 1][v10] + 1
                v9.append('{} {} {} {}'.format(v5 + 1, v10 + 1, v5 + 2, v10 + 1))
                v7 += 1
    else:
        for v10 in range(v3 - 1, -1, -1):
            if v4[v5][v10] % 2 == 0:
                continue
            if not v10 == 0:
                v4[v5][v10] = v4[v5][v10] - 1
                v4[v5][v10 - 1] = v4[v5][v10 - 1] + 1
                v9.append('{} {} {} {}'.format(v5 + 1, v10 + 1, v5 + 1, v10))
                v7 += 1
            elif v5 != v2 - 1:
                v4[v5][v10] = v4[v5][v10] - 1
                v4[v5 + 1][v10] = v4[v5 + 1][v10] + 1
                v9.append('{} {} {} {}'.format(v5 + 1, v10 + 1, v5 + 2, v10 + 1))
                v7 += 1
print(v7)
for v11 in v9:
    print(v11)
