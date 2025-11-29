class C1:

    def maxProfit(self, a1):
        v1 = float('inf')
        v2 = 0
        v3 = float('inf')
        v4 = 0
        for v5 in a1:
            v1 = min(v1, v5)
            v2 = max(v2, v5 - v1)
            v3 = min(v3, v5 - v2)
            v4 = max(v4, v5 - v3)
        return v4
