class C1(object):

    def minStartValue(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v2 += v3
            v1 = min(v1, v2)
        return 1 - v1
