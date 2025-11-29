class C1(object):

    def getMaximumConsecutive(self, a1):
        """
        """
        a1.sort()
        v1 = 1
        for v2 in a1:
            if v2 > v1:
                break
            v1 += v2
        return v1
