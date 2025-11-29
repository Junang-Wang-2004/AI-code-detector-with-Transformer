class C1(object):

    def stoneGameII(self, a1):
        """
        """

        def dp(a1, a2, a3, a4):
            if a3 + 2 * a4 >= len(a1):
                return a1[a3]
            if (a3, a4) not in a2:
                a2[a3, a4] = a1[a3] - min((dp(a1, a2, a3 + x, max(a4, x)) for v1 in range(1, 2 * a4 + 1)))
            return a2[a3, a4]
        for v1 in reversed(range(len(a1) - 1)):
            a1[v1] += a1[v1 + 1]
        return dp(a1, {}, 0, 1)
