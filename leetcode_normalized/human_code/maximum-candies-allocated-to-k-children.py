class C1(object):

    def maximumCandies(self, a1, a2):
        """
        """

        def check(a1):
            return sum((c // a1 for v1 in a1)) >= a2
        v1, v2 = (1, max(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
