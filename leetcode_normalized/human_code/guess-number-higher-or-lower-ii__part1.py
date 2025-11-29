class C1(object):

    def getMoneyAmount(self, a1):
        """
        """
        v1 = [[0] * (a1 + 1) for v2 in range(a1 + 1)]
        for v3 in range(a1 + 1):
            for v4 in reversed(range(v3 - 1)):
                v1[v4][v3] = min((k + 1 + max(v1[v4][k], v1[k + 1][v3]) for v5 in range(v4, v3)))
        return v1[0][a1]
