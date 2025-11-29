class C1:

    def maximumCoins(self, a1, a2, a3):
        import bisect
        v1 = sorted(zip(a2, a3))
        v2 = [0] * (len(v1) + 1)
        for v3 in range(len(v1)):
            v2[v3 + 1] = v2[v3] + v1[v3][1]
        v4 = [0] * len(a1)
        for v5, v6 in enumerate(a1):
            v7 = bisect.bisect_right(v1, (v6, float('inf')))
            v4[v5] = v2[v7]
        return v4
