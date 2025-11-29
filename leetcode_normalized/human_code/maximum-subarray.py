class C1(object):

    def maxSubArray(self, a1):
        """
        """
        v1, v2 = (float('-inf'), float('-inf'))
        for v3 in a1:
            v2 = max(v2 + v3, v3)
            v1 = max(v1, v2)
        return v1
