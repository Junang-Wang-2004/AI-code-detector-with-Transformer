class C1:

    def maximumTotalSum(self, a1):
        v1 = sorted(a1, reverse=True)
        v2 = 0
        v3 = float('inf')
        for v4 in v1:
            v5 = min(v4, v3 - 1)
            if v5 < 1:
                return -1
            v2 += v5
            v3 = v5
        return v2
