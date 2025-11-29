class C1(object):

    def maxIncreasingGroups(self, a1):
        """
        """
        a1.sort()
        v1 = v2 = 0
        for v3 in a1:
            v2 += v3
            if v2 >= v1 + 1:
                v2 -= v1 + 1
                v1 += 1
        return v1
