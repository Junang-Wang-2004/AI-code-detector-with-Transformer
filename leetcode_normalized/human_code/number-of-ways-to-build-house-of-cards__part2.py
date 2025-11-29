class C1(object):

    def houseOfCards(self, a1):
        """
        """
        v1 = [[0] * (a1 + 1) for v2 in range((a1 + 1) // 3 + 1)]
        v1[0][0] = 1
        for v3 in range(1, (a1 + 1) // 3 + 1):
            for v4 in range(3 * v3 - 1, a1 + 1):
                v1[v3][v4] = sum((v1[j][v4 - (3 * v3 - 1)] for v5 in range(v3)))
        return sum((v1[v3][a1] for v3 in range((a1 + 1) // 3 + 1)))
