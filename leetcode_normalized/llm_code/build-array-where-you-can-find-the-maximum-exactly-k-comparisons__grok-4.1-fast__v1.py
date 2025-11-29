class C1(object):

    def numOfArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = [[0] * (a3 + 1) for v3 in range(a2 + 1)]
        for v4 in range(1, a2 + 1):
            v2[v4][1] = 1
        for v5 in range(2, a1 + 1):
            v6 = [[0] * (a2 + 1) for v3 in range(a3 + 1)]
            for v7 in range(a3 + 1):
                for v4 in range(1, a2 + 1):
                    v6[v7][v4] = (v6[v7][v4 - 1] + v2[v4][v7]) % v1
            v8 = [[0] * (a3 + 1) for v3 in range(a2 + 1)]
            for v4 in range(1, a2 + 1):
                for v7 in range(1, a3 + 1):
                    v9 = v2[v4][v7] * v4 % v1
                    v10 = v6[v7 - 1][v4 - 1]
                    v8[v4][v7] = (v9 + v10) % v1
            v2 = v8
        return sum((v2[v4][a3] for v4 in range(1, a2 + 1))) % v1
