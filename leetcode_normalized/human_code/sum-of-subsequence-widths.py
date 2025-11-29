class C1(object):

    def sumSubseqWidths(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 1)
        a1.sort()
        for v4 in range(len(a1)):
            v2 = (v2 + (a1[v4] - a1[len(a1) - 1 - v4]) * v3 % v1) % v1
            v3 = (v3 << 1) % v1
        return v2
