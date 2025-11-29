class C1(object):

    def divisorSubstrings(self, a1, a2):
        """
        """
        v1 = v2 = 0
        v3 = list(map(int, str(a1)))
        v4 = 10 ** (a2 - 1)
        for v5, v6 in enumerate(v3):
            if v5 - a2 >= 0:
                v2 -= v3[v5 - a2] * v4
            v2 = v2 * 10 + v6
            if v5 + 1 >= a2:
                v1 += int(v2 and a1 % v2 == 0)
        return v1
