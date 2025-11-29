class C1(object):

    def minDays(self, a1):
        """
        """

        def memoization(a1, a2):
            if a2 <= 1:
                return a2
            if a2 not in a1:
                a1[a2] = 1 + min(a2 % 2 + memoization(a1, a2 // 2), a2 % 3 + memoization(a1, a2 // 3))
            return a1[a2]
        v1 = {}
        return memoization(v1, a1)
