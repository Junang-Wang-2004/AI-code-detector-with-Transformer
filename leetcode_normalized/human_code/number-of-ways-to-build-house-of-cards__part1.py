class C1(object):

    def houseOfCards(self, a1):
        """
        """
        v1 = [0] * (a1 + 1)
        v1[0] = 1
        for v2 in range(1, (a1 + 1) // 3 + 1):
            for v3 in reversed(range(3 * v2 - 1, a1 + 1)):
                v1[v3] += v1[v3 - (3 * v2 - 1)]
        return v1[a1]
