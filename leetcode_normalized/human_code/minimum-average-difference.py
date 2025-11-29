class C1(object):

    def minimumAverageDifference(self, a1):
        """
        """
        v1 = sum(a1)
        v2, v3 = (float('inf'), -1)
        v4 = 0
        for v5, v6 in enumerate(a1):
            v4 += v6
            v7 = v4 // (v5 + 1)
            v8 = (v1 - v4) // (len(a1) - (v5 + 1)) if v5 + 1 < len(a1) else 0
            v9 = abs(v7 - v8)
            if v9 < v2:
                v2, v3 = (v9, v5)
        return v3
