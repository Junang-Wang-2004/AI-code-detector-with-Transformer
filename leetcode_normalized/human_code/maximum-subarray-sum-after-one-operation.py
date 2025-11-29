class C1(object):

    def maxSumAfterOperation(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = 0
        for v4 in a1:
            v5 = max(v4, v4 + v2)
            v6 = max(v4 * v4, v4 * v4 + v2, v4 + v1)
            v3 = max(v3, v6)
            v1, v2 = (v6, v5)
        return v3
