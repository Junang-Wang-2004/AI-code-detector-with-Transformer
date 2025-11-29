v1, v2 = (int(input()), 10 ** 9 + 7)
v3 = [[[0] * 4] * 4] * 101
'\n長さ0の文字列は1\n0, 1, 2に関する制約しかないので、Sは、333Sと考えても問題がない\n'
v3[0][3][3][3] = 1
for v4 in range(v1):
    for v5 in range(4):
        for v6 in range(4):
            for v7 in range(4):
                if v3[v4][v5][v6][v7] == 0:
                    continue
                for v8 in range(v8):
                    if v8 == 2 and v5 == 1 and (v6 == 0):
                        continue
                    if v8 == 2 and v5 == 0 and (v6 == 1):
                        continue
                    if v8 == 1 and v5 == 2 and (v6 == 0):
                        continue
                    if v8 == 2 and v5 == 1 and (v7 == 0):
                        continue
                    if v8 == 2 and v6 == 1 and (v7 == 0):
                        continue
                    v3[v4 + 1][v8][v5][v6] += v3[v4][v5][v6][v7]
                    v3[v4 + 1][v8][v5][v6] %= v2
v9 = 0
for v5 in range(4):
    for v6 in range(4):
        for v7 in range(4):
            v9 += v3[v1][v5][v6][v7]
            v9 %= v2
print(v9)
