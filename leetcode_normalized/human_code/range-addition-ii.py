class C1(object):

    def maxCount(self, a1, a2, a3):
        """
        """
        for v1 in a3:
            a1 = min(a1, v1[0])
            a2 = min(a2, v1[1])
        return a1 * a2
