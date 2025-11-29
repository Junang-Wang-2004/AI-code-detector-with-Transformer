class C1(object):

    def smallestRangeII(self, a1, a2):
        """
        """
        a1.sort()
        v1 = a1[-1] - a1[0]
        for v2 in range(len(a1) - 1):
            v1 = min(v1, max(a1[-1] - a2, a1[v2] + a2) - min(a1[0] + a2, a1[v2 + 1] - a2))
        return v1
