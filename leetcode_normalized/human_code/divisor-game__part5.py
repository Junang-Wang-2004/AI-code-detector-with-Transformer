class C1(object):

    def divisorGame(self, a1):
        """
        """

        def factors(a1):
            for v1 in range(1, a1 + 1):
                if a1 % v1:
                    continue
                yield v1

        def memoization(a1):
            if lookup[a1] is None:
                lookup[a1] = any((not memoization(a1 - i) for v1 in factors(a1) if v1 != a1))
            return lookup[a1]
        v1 = [None] * (a1 + 1)
        return memoization(a1)
