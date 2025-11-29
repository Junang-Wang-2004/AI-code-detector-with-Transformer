class C1:

    def maximumProfit(self, a1, a2):
        if not a1 or a2 == 0:
            return 0
        v1 = [-float('inf')] * (a2 + 1)
        v2 = [0] + [-float('inf')] * a2
        for v3 in a1:
            for v4 in range(a2, 0, -1):
                v1[v4] = max(v1[v4], v2[v4 - 1] - v3)
                v2[v4] = max(v2[v4], v1[v4] + v3)
        return max(v2)
