class C1(object):

    def minCostToEqualizeArray(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = max(a1)
        v4 = v3 * v2 - sum(a1)
        if v2 <= 2 or a2 * 2 <= a3:
            return v4 * a2 % v1
        v5 = float('inf')
        v6 = min(a1)
        v7 = max(v3 - v6 - (v4 - (v3 - v6)), 0)
        v8 = v4 - v7
        v5 = min(v5, (v7 + v8 % 2) * a2 + v8 // 2 * a3)
        v9, v7 = divmod(v7, v2 - 2)
        v4 += v2 * v9
        v8 = v4 - v7
        v5 = min(v5, (v7 + v8 % 2) * a2 + v8 // 2 * a3)
        for v10 in range(2):
            v4 += v2
            v5 = min(v5, v4 % 2 * a2 + v4 // 2 * a3)
        return v5 % v1
