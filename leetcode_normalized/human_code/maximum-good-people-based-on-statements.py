class C1(object):

    def maximumGood(self, a1):
        """
        """

        def check(a1):
            return all((a1 >> j & 1 == a1[i][j] for v1 in range(len(a1)) if a1 >> v1 & 1 for v2 in range(len(a1[v1])) if a1[v1][v2] != 2))

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        v1 = 0
        for v2 in range(1 << len(a1)):
            if check(v2):
                v1 = max(v1, popcount(v2))
        return v1
