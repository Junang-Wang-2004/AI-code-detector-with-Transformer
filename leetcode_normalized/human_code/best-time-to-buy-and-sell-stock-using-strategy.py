class C1(object):

    def maxProfit(self, a1, a2, a3):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            v2 += a1[v3] * (0 if v3 < a3 // 2 else 1) if v3 < a3 else a1[v3] * a2[v3]
            v1 += a1[v3] * a2[v3]
        v1 = max(v1, v2)
        for v3 in range(a3, len(a1)):
            v2 += a1[v3 - a3] * a2[v3 - a3] + (a1[v3] - a1[v3 - a3 // 2]) - a1[v3] * a2[v3]
            v1 = max(v1, v2)
        return v1
