class C1(object):

    def maxCoins(self, a1):
        """
        """
        v1 = [1] + [i for v2 in a1 if v2 > 0] + [1]
        v3 = len(v1)
        v4 = [[0 for v5 in range(v3)] for v5 in range(v3)]
        for v6 in range(2, v3):
            for v7 in range(v3 - v6):
                v8 = v7 + v6
                for v2 in range(v7 + 1, v8):
                    v4[v7][v8] = max(v4[v7][v8], v1[v7] * v1[v2] * v1[v8] + v4[v7][v2] + v4[v2][v8])
        return v4[0][-1]
