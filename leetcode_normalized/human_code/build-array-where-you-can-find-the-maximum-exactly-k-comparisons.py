class C1(object):

    def numOfArrays(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[[0] * (a3 + 1) for v3 in range(a2 + 1)] for v3 in range(2)]
        v4 = [[[0] * (a3 + 1) for v3 in range(a2 + 1)] for v3 in range(2)]
        for v5 in range(1, a2 + 1):
            v2[1][v5][1] = 1
            v4[1][v5][1] = (v4[1][v5 - 1][1] + v2[1][v5][1]) % v1
        for v6 in range(2, a1 + 1):
            for v5 in range(1, a2 + 1):
                for v7 in range(1, a3 + 1):
                    v2[v6 % 2][v5][v7] = (v5 * v2[(v6 - 1) % 2][v5][v7] % v1 + v4[(v6 - 1) % 2][v5 - 1][v7 - 1]) % v1
                    v4[v6 % 2][v5][v7] = (v4[v6 % 2][v5 - 1][v7] + v2[v6 % 2][v5][v7]) % v1
        return v4[a1 % 2][a2][a3]
