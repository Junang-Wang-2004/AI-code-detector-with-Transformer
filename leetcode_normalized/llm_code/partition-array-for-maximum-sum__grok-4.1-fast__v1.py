class C1:

    def maxSumAfterPartitioning(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(1, v1 + 1):
            v4 = 0
            v5 = max(0, v3 - a2)
            for v6 in range(v3 - 1, v5 - 1, -1):
                v4 = max(v4, a1[v6])
                v2[v3] = max(v2[v3], v2[v6] + v4 * (v3 - v6))
        return v2[v1]
