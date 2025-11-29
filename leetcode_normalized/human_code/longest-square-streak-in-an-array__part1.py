class C1(object):

    def longestSquareStreak(self, a1):
        """
        """
        v1 = sorted(set(a1))
        v2 = {x for v3 in v1 if v3 % 2 < 2}
        v4 = 0
        for v3 in v1:
            v5, v6 = (v3 ** 2, 1)
            while v5 in v2:
                v2.remove(v5)
                v6 += 1
                v5 *= v5
            v4 = max(v4, v6)
        return v4 if v4 != 1 else -1
