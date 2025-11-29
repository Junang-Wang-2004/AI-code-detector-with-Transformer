class C1(object):

    def arrangeCoins(self, a1):
        """
        """

        def check(a1, a2):
            return a1 * (a1 + 1) <= 2 * a2
        v1, v2 = (1, a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(v3, a1):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
