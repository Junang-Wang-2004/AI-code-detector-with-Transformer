class C1(object):

    def countHousePlacements(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (1, 2)
        for v4 in range(a1 - 1):
            v2, v3 = (v3, (v2 + v3) % v1)
        return pow(v3, 2, v1)
