class C1:

    def maxKilledEnemies(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]
        v5 = [[0] * v2 for v4 in range(v1)]
        v6 = [[0] * v2 for v4 in range(v1)]
        v7 = [[0] * v2 for v4 in range(v1)]
        for v8 in range(v1):
            v9 = 0
            for v10 in range(v2):
                if a1[v8][v10] == 'W':
                    v9 = 0
                else:
                    v3[v8][v10] = v9
                    if a1[v8][v10] == 'E':
                        v9 += 1
            v9 = 0
            for v10 in range(v2 - 1, -1, -1):
                if a1[v8][v10] == 'W':
                    v9 = 0
                else:
                    v5[v8][v10] = v9
                    if a1[v8][v10] == 'E':
                        v9 += 1
        for v10 in range(v2):
            v9 = 0
            for v8 in range(v1):
                if a1[v8][v10] == 'W':
                    v9 = 0
                else:
                    v6[v8][v10] = v9
                    if a1[v8][v10] == 'E':
                        v9 += 1
            v9 = 0
            for v8 in range(v1 - 1, -1, -1):
                if a1[v8][v10] == 'W':
                    v9 = 0
                else:
                    v7[v8][v10] = v9
                    if a1[v8][v10] == 'E':
                        v9 += 1
        v11 = 0
        for v8 in range(v1):
            for v10 in range(v2):
                if a1[v8][v10] == '0':
                    v12 = v3[v8][v10] + v5[v8][v10] + v6[v8][v10] + v7[v8][v10]
                    if v12 > v11:
                        v11 = v12
        return v11
