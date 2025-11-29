class C1(object):

    def maximumSumScore(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = float('-inf')
        v4 = len(a1) - 1
        for v5 in range(len(a1)):
            v1 += a1[v5]
            v2 += a1[v4]
            v4 -= 1
            v3 = max(v3, v1, v2)
        return v3
