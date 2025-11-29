class C1(object):

    def sellingWood(self, a1, a2, a3):
        """
        """
        v1 = [[0] * (a2 + 1) for v2 in range(a1 + 1)]
        for v3, v4, v5 in a3:
            v1[v3][v4] = v5
        for v2 in range(1, a1 + 1):
            for v6 in range(1, a2 + 1):
                for v7 in range(1, v2 // 2 + 1):
                    v1[v2][v6] = max(v1[v2][v6], v1[v7][v6] + v1[v2 - v7][v6])
                for v7 in range(1, v6 // 2 + 1):
                    v1[v2][v6] = max(v1[v2][v6], v1[v2][v7] + v1[v2][v6 - v7])
        return v1[a1][a2]
