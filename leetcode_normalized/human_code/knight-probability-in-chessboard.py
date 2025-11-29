class C1(object):

    def knightProbability(self, a1, a2, a3, a4):
        """
        """
        v1 = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
        v2 = [[[1 for v3 in range(a1)] for v3 in range(a1)] for v3 in range(2)]
        for v4 in range(1, a2 + 1):
            for v5 in range(a1):
                for v6 in range(a1):
                    v2[v4 % 2][v5][v6] = 0
                    for v7 in v1:
                        v8, v9 = (v5 + v7[0], v6 + v7[1])
                        if 0 <= v9 < a1 and 0 <= v8 < a1:
                            v2[v4 % 2][v5][v6] += 0.125 * v2[(v4 - 1) % 2][v8][v9]
        return v2[a2 % 2][a3][a4]
