class C1(object):

    def numDupDigitsAtMostN(self, a1):
        """
        """

        def P(a1, a2):
            v1 = 1
            for v2 in range(a2):
                v1 *= a1
                a1 -= 1
            return v1
        v1 = list(map(int, str(a1 + 1)))
        v2 = 0
        for v3 in range(1, len(v1)):
            v2 += P(9, 1) * P(9, v3 - 1)
        v4 = set()
        for v3, v5 in enumerate(v1):
            for v6 in range(1 if v3 == 0 else 0, v5):
                if v6 in v4:
                    continue
                v2 += P(9 - v3, len(v1) - v3 - 1)
            if v5 in v4:
                break
            v4.add(v5)
        return a1 - v2
