class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = sorted(a2 + [0, a1])
        v2 = [[0] * len(v1) for v3 in range(len(v1))]
        for v4 in range(2, len(v1)):
            for v5 in range(len(v1) - v4):
                v2[v5][v5 + v4] = min((v2[v5][j] + v2[j][v5 + v4] for v6 in range(v5 + 1, v5 + v4))) + v1[v5 + v4] - v1[v5]
        return v2[0][len(v1) - 1]
