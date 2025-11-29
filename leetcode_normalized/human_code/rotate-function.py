class C1(object):

    def maxRotateFunction(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = 0
        for v3 in range(len(a1)):
            v2 += v3 * a1[v3]
        v4 = v2
        for v3 in range(1, len(a1) + 1):
            v2 += v1 - len(a1) * a1[-v3]
            v4 = max(v4, v2)
        return v4
