class C1:

    def knightProbability(self, a1: int, a2: int, a3: int, a4: int) -> float:
        v1 = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        v2 = [[0.0] * a1 for v3 in range(a1)]
        v2[a3][a4] = 1.0
        for v3 in range(a2):
            v4 = [[0.0] * a1 for v3 in range(a1)]
            for v5 in range(a1):
                for v6 in range(a1):
                    v7 = v2[v5][v6] / 8
                    for v8, v9 in v1:
                        v10 = v5 + v8
                        v11 = v6 + v9
                        if 0 <= v10 < a1 and 0 <= v11 < a1:
                            v4[v10][v11] += v7
            v2 = v4
        return sum((sum(r) for v12 in v2))
