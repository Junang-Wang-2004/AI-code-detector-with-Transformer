class C1(object):

    def countWinningSequences(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = len(a1)
        v3 = v2
        v4 = {'F': 0, 'W': 1, 'E': 2}
        v5 = [v4[ch] for v6 in a1]
        v7 = [[0] * (2 * v2 + 1) for v8 in range(3)]
        for v9 in range(3):
            v10 = (v9 - v5[0] + 1) % 3 - 1
            v7[v9][v10 + v3] = 1
        for v11 in range(1, v2):
            v12 = [[0] * (2 * v2 + 1) for v8 in range(3)]
            for v13 in range(3):
                for v14 in range(2 * v2 + 1):
                    if v7[v13][v14] == 0:
                        continue
                    v15 = v14 - v3
                    for v9 in range(3):
                        if v9 == v13:
                            continue
                        v10 = (v9 - v5[v11] + 1) % 3 - 1
                        v16 = v15 + v10 + v3
                        if 0 <= v16 < 2 * v2 + 1:
                            v12[v9][v16] = (v12[v9][v16] + v7[v13][v14]) % v1
            v7 = v12
        v17 = 0
        for v9 in range(3):
            for v14 in range(v3 + 1, 2 * v2 + 1):
                v17 = (v17 + v7[v9][v14]) % v1
        return v17
