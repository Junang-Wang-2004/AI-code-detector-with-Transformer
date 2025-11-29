class C1(object):

    def countPalindromes(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * 10
        v3 = [[[0] * 10 for v4 in range(10)] for v4 in range(len(a1) + 1)]
        for v5 in range(len(a1)):
            v3[v5 + 1] = [[v3[v5][i][j] for v6 in range(10)] for v7 in range(10)]
            for v7 in range(10):
                v3[v5 + 1][int(a1[v5])][v7] += v2[v7]
            v2[int(a1[v5])] += 1
        v2 = [0] * 10
        v8 = [[0] * 10 for v4 in range(10)]
        v9 = 0
        for v5 in reversed(range(len(a1))):
            for v7 in range(10):
                for v6 in range(10):
                    v9 = (v9 + v3[v5][v7][v6] * v8[v7][v6]) % v1
            for v7 in range(10):
                v8[int(a1[v5])][v7] += v2[v7]
            v2[int(a1[v5])] += 1
        return v9
