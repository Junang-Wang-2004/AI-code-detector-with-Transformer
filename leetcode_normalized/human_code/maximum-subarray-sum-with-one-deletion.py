class C1(object):

    def maximumSum(self, a1):
        """
        """
        v1, v2, v3 = (float('-inf'), float('-inf'), float('-inf'))
        for v4 in a1:
            v3 = max(v2, v3 + v4, v4)
            v1 = max(v1, v3)
            v2 = max(v2 + v4, v4)
        return v1
