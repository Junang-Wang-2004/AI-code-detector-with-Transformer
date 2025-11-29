class C1:

    def maximumProfit(self, a1, a2, a3):
        v1 = [0] * (a3 + 1)

        def enhance(a1, a2, a3):
            for v1 in range(a3, a1 - 1, -1):
                v1[v1] = max(v1[v1], v1[v1 - a1] + a2)
        for v2, v3 in zip(a1, a2):
            v4 = v3 - v2
            if v4 > 0:
                enhance(v2, v4, a3)
        return v1[a3]
