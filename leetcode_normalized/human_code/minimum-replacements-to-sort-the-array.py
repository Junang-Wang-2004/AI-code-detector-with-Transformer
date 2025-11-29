class C1(object):

    def minimumReplacement(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = 0
        v2 = a1[-1]
        for v3 in reversed(a1):
            v4 = ceil_divide(v3, v2)
            v1 += v4 - 1
            v2 = v3 // v4
        return v1
