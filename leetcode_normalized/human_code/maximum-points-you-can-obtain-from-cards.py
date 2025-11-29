class C1(object):

    def maxScore(self, a1, a2):
        """
        """
        v1, v2, v3, v4 = (float('inf'), 0, 0, 0)
        for v5, v6 in enumerate(a1):
            v2 += v6
            v3 += v6
            if v5 - v4 + 1 > len(a1) - a2:
                v3 -= a1[v4]
                v4 += 1
            if v5 - v4 + 1 == len(a1) - a2:
                v1 = min(v1, v3)
        return v2 - v1
