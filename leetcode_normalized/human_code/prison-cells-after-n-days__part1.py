class C1(object):

    def prisonAfterNDays(self, a1, a2):
        """
        """
        a2 -= max(a2 - 1, 0) // 14 * 14
        for v2 in range(a2):
            a1 = [0] + [a1[v2 - 1] ^ a1[v2 + 1] ^ 1 for v2 in range(1, 7)] + [0]
        return a1
