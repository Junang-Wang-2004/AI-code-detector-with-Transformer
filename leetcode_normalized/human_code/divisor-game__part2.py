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
        v1 = factors(a1)
        v2 = [False] * (a1 + 1)
        for v3 in range(2, a1 + 1):
            v2[v3] = any((not v2[v3 - j] for v4 in v1[v3] if v4 != v3))
        return v2[-1]
