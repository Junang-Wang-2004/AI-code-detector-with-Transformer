class C1(object):

    def prisonAfterNDays(self, a1, a2):
        """
        """
        a1 = tuple(a1)
        v2 = {}
        while a2:
            v2[a1] = a2
            a2 -= 1
            a1 = tuple([0] + [a1[i - 1] ^ a1[i + 1] ^ 1 for v4 in range(1, 7)] + [0])
            if a1 in v2:
                assert v2[a1] - a2 in (1, 7, 14)
                a2 %= v2[a1] - a2
                break
        while a2:
            a2 -= 1
            a1 = tuple([0] + [a1[v4 - 1] ^ a1[v4 + 1] ^ 1 for v4 in range(1, 7)] + [0])
        return list(a1)
