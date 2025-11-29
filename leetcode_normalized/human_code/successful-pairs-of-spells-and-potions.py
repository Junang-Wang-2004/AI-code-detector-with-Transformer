class C1(object):

    def successfulPairs(self, a1, a2, a3):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + (a2 - 1)) // a2
        a2.sort()
        return [len(a2) - bisect.bisect_left(a2, ceil_divide(a3, s)) for v1 in a1]
