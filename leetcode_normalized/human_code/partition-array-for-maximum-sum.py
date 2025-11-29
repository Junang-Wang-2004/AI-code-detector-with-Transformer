class C1(object):

    def maxSumAfterPartitioning(self, a1, a2):
        """
        """
        v1 = a2 + 1
        v2 = [0] * v1
        for v3 in range(len(a1)):
            v4 = 0
            for v5 in range(1, min(a2, v3 + 1) + 1):
                v4 = max(v4, a1[v3 - v5 + 1])
                v2[v3 % v1] = max(v2[v3 % v1], (v2[(v3 - v5) % v1] if v3 >= v5 else 0) + v4 * v5)
        return v2[(len(a1) - 1) % v1]
