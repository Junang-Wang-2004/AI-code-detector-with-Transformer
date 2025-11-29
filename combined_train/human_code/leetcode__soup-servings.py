class C1(object):

    def soupServings(self, a1):
        """
        """

        def dp(a1, a2, a3):
            if (a1, a2) in a3:
                return a3[a1, a2]
            if a1 <= 0 and a2 <= 0:
                return 0.5
            if a1 <= 0:
                return 1.0
            if a2 <= 0:
                return 0.0
            a3[a1, a2] = 0.25 * (dp(a1 - 4, a2, a3) + dp(a1 - 3, a2 - 1, a3) + dp(a1 - 2, a2 - 2, a3) + dp(a1 - 1, a2 - 3, a3))
            return a3[a1, a2]
        if a1 >= 4800:
            return 1.0
        v1 = {}
        a1 = (a1 + 24) // 25
        return dp(a1, a1, v1)
