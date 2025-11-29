class C1(object):

    def minimizeArrayValue(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = v2 = 0
        for v3, v4 in enumerate(a1):
            v2 += v4
            v1 = max(v1, ceil_divide(v2, v3 + 1))
        return v1
