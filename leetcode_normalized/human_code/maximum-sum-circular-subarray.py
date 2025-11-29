class C1(object):

    def maxSubarraySumCircular(self, a1):
        """
        """
        v1, v2, v3, v4, v5 = (0, -float('inf'), 0, float('inf'), 0)
        for v6 in a1:
            v3 = max(v3 + v6, v6)
            v2 = max(v2, v3)
            v5 = min(v5 + v6, v6)
            v4 = min(v4, v5)
            v1 += v6
        return max(v2, v1 - v4) if v2 >= 0 else v2
