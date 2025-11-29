class C1(object):

    def strangePrinter(self, a1):
        """
        """

        def dp(a1, a2, a3, a4):
            if a2 > a3:
                return 0
            if (a2, a3) not in a4:
                a4[a2, a3] = dp(a1, a2, a3 - 1, a4) + 1
                for v1 in range(a2, a3):
                    if a1[v1] == a1[a3]:
                        a4[a2, a3] = min(a4[a2, a3], dp(a1, a2, v1, a4) + dp(a1, v1 + 1, a3 - 1, a4))
            return a4[a2, a3]
        v1 = {}
        return dp(a1, 0, len(a1) - 1, v1)
