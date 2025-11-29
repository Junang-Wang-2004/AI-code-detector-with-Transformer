class C1(object):

    def countPathsWithXorValue(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = 16
        v3 = len(a1)
        v4 = len(a1[0])
        v5 = [[0] * v2 for v6 in range(v4)]
        v5[0][0] = 1
        for v7 in range(v3):
            v8 = [[0] * v2 for v6 in range(v4)]
            for v9 in range(v4):
                v10 = a1[v7][v9]
                for v11 in range(v2):
                    v12 = v10 ^ v11
                    v8[v9][v12] = (v8[v9][v12] + v5[v9][v11]) % v1
            for v9 in range(1, v4):
                v10 = a1[v7][v9]
                for v11 in range(v2):
                    v12 = v10 ^ v11
                    v8[v9][v12] = (v8[v9][v12] + v8[v9 - 1][v11]) % v1
            v5 = v8
        return v5[v4 - 1][a2]
