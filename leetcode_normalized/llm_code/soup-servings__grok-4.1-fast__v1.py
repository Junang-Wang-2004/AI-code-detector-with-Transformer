class C1:

    def soupServings(self, a1):
        if a1 >= 4800:
            return 1.0
        v1 = (a1 + 24) // 25
        v2 = [[0.0] * (v1 + 1) for v3 in range(v1 + 1)]
        v4 = [(4, 0), (3, 1), (2, 2), (1, 3)]
        for v5 in range(v1 + 1):
            for v6 in range(v1 + 1):
                if v5 == 0 and v6 == 0:
                    v2[0][0] = 0.5
                elif v5 == 0:
                    v2[0][v6] = 1.0
                elif v6 == 0:
                    v2[v5][0] = 0.0
                else:
                    v7 = 0.0
                    for v8, v9 in v4:
                        v10 = v5 - v8
                        v11 = v6 - v9
                        if v10 <= 0 and v11 <= 0:
                            v7 += 0.5
                        elif v10 <= 0:
                            v7 += 1.0
                        elif v11 <= 0:
                            v7 += 0.0
                        else:
                            v7 += v2[v10][v11]
                    v2[v5][v6] = v7 / 4
        return v2[v1][v1]
