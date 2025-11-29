class C1(object):

    def addRungs(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + (a2 - 1)) // a2
        v1 = v2 = 0
        for v3 in a1:
            v1 += ceil_divide(v3 - v2, a2) - 1
            v2 = v3
        return v1
