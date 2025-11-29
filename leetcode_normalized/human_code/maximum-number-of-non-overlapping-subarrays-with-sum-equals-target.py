class C1(object):

    def maxNonOverlapping(self, a1, a2):
        """
        """
        v1 = {0: -1}
        v2, v3, v4 = (0, 0, -1)
        for v5, v6 in enumerate(a1):
            v3 += v6
            if v3 - a2 in v1 and v1[v3 - a2] >= v4:
                v4 = v5
                v2 += 1
            v1[v3] = v5
        return v2
