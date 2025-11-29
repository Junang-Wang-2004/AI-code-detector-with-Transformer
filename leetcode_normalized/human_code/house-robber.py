class C1(object):

    def rob(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v1, v2 = (v2, max(v1 + v3, v2))
        return v2
