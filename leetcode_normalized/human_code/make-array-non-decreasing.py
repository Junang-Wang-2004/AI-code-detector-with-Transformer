class C1(object):

    def maximumPossibleSize(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v2 <= v3:
                v2 = v3
                v1 += 1
        return v1
