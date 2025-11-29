class C1(object):

    def maximumSumScore(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = 0
        v3 = float('-inf')
        for v4 in a1:
            v2 += v4
            v3 = max(v3, v2, v1 - v2 + v4)
        return v3
