class C1(object):

    def minScoreTriangulation(self, a1):
        """
        """
        v1 = [[0 for v2 in range(len(a1))] for v2 in range(len(a1))]
        for v3 in range(3, len(a1) + 1):
            for v4 in range(len(a1) - v3 + 1):
                v5 = v4 + v3 - 1
                v1[v4][v5] = float('inf')
                for v6 in range(v4 + 1, v5):
                    v1[v4][v5] = min(v1[v4][v5], v1[v4][v6] + v1[v6][v5] + a1[v4] * a1[v5] * a1[v6])
        return v1[0][-1]
