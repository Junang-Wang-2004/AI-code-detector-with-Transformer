class C1(object):

    def maxAbsValExpr(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in [1, -1]:
            for v3 in [1, -1]:
                v4 = float('inf')
                for v5 in range(len(a1)):
                    v6 = v2 * a1[v5] + v3 * a2[v5] + v5
                    v1 = max(v1, v6 - v4)
                    v4 = min(v4, v6)
        return v1
