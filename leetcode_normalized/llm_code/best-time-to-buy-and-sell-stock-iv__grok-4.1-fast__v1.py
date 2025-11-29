class C1:

    def maxProfit(self, a1, a2):
        v1 = len(a2)
        if v1 <= 1:
            return 0
        if a1 >= v1 // 2:
            v2 = 0
            for v3 in range(v1 - 1):
                v4 = a2[v3 + 1] - a2[v3]
                if v4 > 0:
                    v2 += v4
            return v2
        v5 = [-float('inf')] * (a1 + 1)
        v6 = [0] * (a1 + 1)
        for v7 in a2:
            for v8 in range(1, a1 + 1):
                v5[v8] = max(v5[v8], v6[v8 - 1] - v7)
                v6[v8] = max(v6[v8], v5[v8] + v7)
        return v6[a1]
