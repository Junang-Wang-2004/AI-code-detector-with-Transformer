class C1(object):

    def maximumElementAfterDecrementingAndRearranging(self, a1):
        """
        """
        a1.sort()
        v1 = 1
        for v2 in range(1, len(a1)):
            v1 = min(v1 + 1, a1[v2])
        return v1
