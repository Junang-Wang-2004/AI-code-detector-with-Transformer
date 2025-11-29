class C1(object):

    def minCost(self, a1, a2, a3):
        """
        """
        a3[0][0] = a3[a1 - 1][a2 - 1] = 0
        v1 = [0] * a2
        for v2 in range(a1):
            for v3 in range(a2):
                v4 = 0 if (v2, v3) == (0, 0) else float('inf')
                if v2 - 1 >= 0:
                    v4 = min(v4, v1[v3])
                if v3 - 1 >= 0:
                    v4 = min(v4, v1[v3 - 1])
                v1[v3] = v4 + a3[v2][v3] + (v2 + 1) * (v3 + 1)
        return v1[a2 - 1]
