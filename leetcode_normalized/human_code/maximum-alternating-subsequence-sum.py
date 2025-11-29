class C1(object):

    def maxAlternatingSum(self, a1):
        """
        """
        v1 = a1[0]
        for v2 in range(len(a1) - 1):
            v1 += max(a1[v2 + 1] - a1[v2], 0)
        return v1
