class C1:

    def stringCount(self, a1):
        v1 = 10 ** 9 + 7
        v2 = [[[0] * 3 for v3 in range(2)] for v3 in range(2)]
        v2[0][0][0] = 1
        for v3 in range(a1):
            v4 = [[[0] * 3 for v3 in range(2)] for v3 in range(2)]
            for v5 in range(2):
                for v6 in range(2):
                    for v7 in range(3):
                        v8 = v2[v5][v6][v7]
                        v4[v5][v6][v7] = (v4[v5][v6][v7] + v8 * 23) % v1
                        v4[1][v6][v7] = (v4[1][v6][v7] + v8) % v1
                        v4[v5][1][v7] = (v4[v5][1][v7] + v8) % v1
                        v9 = min(v7 + 1, 2)
                        v4[v5][v6][v9] = (v4[v5][v6][v9] + v8) % v1
            v2 = v4
        return v2[1][1][2]
