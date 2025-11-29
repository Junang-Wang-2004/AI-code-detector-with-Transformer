class C1(object):

    def balancedStringSplit(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v2 += 1 if v3 == 'L' else -1
            if v2 == 0:
                v1 += 1
        return v1
