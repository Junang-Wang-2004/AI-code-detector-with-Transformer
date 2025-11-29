class C1(object):

    def countCombinations(self, a1, a2):
        """
        """
        v1 = {'rook': [(0, 1), (1, 0), (0, -1), (-1, 0)], 'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)], 'queen': [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]}
        v2 = 2 ** 7 - 1

        def backtracking(a1, a2, a3, a4):
            if a3 == len(a1):
                return 1
            v1 = 0
            v2, v3 = a2[a3]
            v2, v3 = (v2 - 1, v3 - 1)
            v4 = v2
            if not a4[v2][v3] & v4:
                a4[v2][v3] += v4
                v1 += backtracking(a1, a2, a3 + 1, a4)
                a4[v2][v3] -= v4
            for v5, v6 in v1[a1[a3]]:
                v7, v8, v9 = (1, v2 + v5, v3 + v6)
                v4 = v2
                while 0 <= v8 < 8 and 0 <= v9 < 8 and (not a4[v8][v9] & v7):
                    a4[v8][v9] += v7
                    v4 -= v7
                    if not a4[v8][v9] & v4:
                        a4[v8][v9] += v4
                        v1 += backtracking(a1, a2, a3 + 1, a4)
                        a4[v8][v9] -= v4
                    v7, v8, v9 = (v7 << 1, v8 + v5, v9 + v6)
                while v7 >> 1:
                    v7, v8, v9 = (v7 >> 1, v8 - v5, v9 - v6)
                    a4[v8][v9] -= v7
            return v1
        return backtracking(a1, a2, 0, [[0] * 8 for v3 in range(8)])
