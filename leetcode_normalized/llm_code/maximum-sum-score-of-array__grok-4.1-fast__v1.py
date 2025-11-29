class C1:

    def maximumSumScore(self, a1):
        v1 = float('-inf')
        v2 = 0
        for v3 in a1:
            v2 += v3
            v1 = max(v1, v2)
        v2 = 0
        for v4 in range(len(a1) - 1, -1, -1):
            v2 += a1[v4]
            v1 = max(v1, v2)
        return v1
