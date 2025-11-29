class C1(object):

    def countExcellentPairs(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1)[2:].count('1')
        v1 = sorted((popcount(x) for v2 in set(a1)))
        v3 = 0
        v4, v5 = (0, len(v1) - 1)
        while v4 <= v5:
            if v1[v4] + v1[v5] < a2:
                v4 += 1
            else:
                v3 += 1 + 2 * (v5 - 1 - v4 + 1)
                v5 -= 1
        return v3
