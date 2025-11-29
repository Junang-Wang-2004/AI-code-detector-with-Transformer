class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        a1.sort()
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = [0] * len(a2)
        for v2, v4 in enumerate(a2):
            v5 = bisect.bisect_left(a1, v4)
            v3[v2] = v4 * v5 - v1[v5] + (v1[-1] - v1[v5] - v4 * (len(a1) - v5))
        return v3
