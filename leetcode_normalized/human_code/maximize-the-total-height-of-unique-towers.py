class C1(object):

    def maximumTotalSum(self, a1):
        """
        """
        a1.sort()
        v1, v2 = (0, a1[-1] + 1)
        for v3 in reversed(a1):
            v2 = min(v3, v2 - 1)
            if v2 == 0:
                return -1
            v1 += v2
        return v1
