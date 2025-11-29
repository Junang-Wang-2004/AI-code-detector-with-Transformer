class C1(object):

    def minimumOperationsToMakeEqual(self, a1, a2):
        """
        """

        def memoization(a1):
            if a2 >= a1:
                return a2 - a1
            if a1 not in lookup:
                lookup[a1] = min(a1 - a2, min((min(a1 % d, d - a1 % d) + memoization(a1 // d + int(d - a1 % d < a1 % d)) + 1 for v1 in (5, 11))))
            return lookup[a1]
        v1 = {}
        return memoization(a1)
