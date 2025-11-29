class C1(object):

    def isCovered(self, a1, a2, a3):
        """
        """
        a1.sort()
        for v1, v2 in a1:
            if v1 <= a2 <= v2:
                a2 = v2 + 1
        return a2 > a3
