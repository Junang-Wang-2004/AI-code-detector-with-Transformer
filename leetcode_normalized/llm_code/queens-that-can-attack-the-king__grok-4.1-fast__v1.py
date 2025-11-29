class C1:

    def queensAttacktheKing(self, a1, a2):
        v1 = [[0] * 8 for v2 in range(8)]
        for v3, v4 in a1:
            v1[v3][v4] = 1
        v5 = []
        v6, v7 = a2
        v8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for v9, v10 in v8:
            v3, v4 = (v6 + v9, v7 + v10)
            while 0 <= v3 < 8 and 0 <= v4 < 8:
                if v1[v3][v4] == 1:
                    v5.append([v3, v4])
                    break
                v3 += v9
                v4 += v10
        return v5
