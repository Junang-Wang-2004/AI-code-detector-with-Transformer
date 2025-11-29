class C1(object):

    def divisorGame(self, a1):
        """
        """

        def factors(a1):
            v1 = [[] for v2 in range(a1 + 1)]
            for v3 in range(1, a1 + 1):
                for v4 in range(v3, a1 + 1, v3):
                    v1[v4].append(v3)
            return v1

        def memoization(a1):
            if lookup[a1] is None:
                lookup[a1] = any((not memoization(a1 - i) for v1 in FACTORS[a1] if v1 != a1))
            return lookup[a1]
        v1 = factors(a1)
        v2 = [None] * (a1 + 1)
        return memoization(a1)
