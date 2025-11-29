class C1(object):

    def average(self, a1):
        """
        """
        v1, v2, v3 = (0, float('inf'), float('-inf'))
        for v4 in a1:
            v1 += v4
            v2, v3 = (min(v2, v4), max(v3, v4))
        return 1.0 * (v1 - v2 - v3) / (len(a1) - 2)
