class C1(object):

    def minCost(self, a1, a2, a3):
        """
        """
        a3[0][0] = a3[a1 - 1][a2 - 1] = 0
        for v1 in range(a1):
            for v2 in range(a2):
                v3 = 0 if (v1, v2) == (0, 0) else float('inf')
                if v1 - 1 >= 0:
                    v3 = min(v3, a3[v1 - 1][v2])
                if v2 - 1 >= 0:
                    v3 = min(v3, a3[v1][v2 - 1])
                a3[v1][v2] += v3 + (v1 + 1) * (v2 + 1)
        return a3[a1 - 1][a2 - 1]
