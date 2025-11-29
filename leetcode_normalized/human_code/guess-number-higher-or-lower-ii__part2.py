class C1(object):

    def getMoneyAmount(self, a1):
        """
        """
        v1 = [[0] * (a1 + 1) for v2 in range(a1 + 1)]
        for v3 in reversed(range(a1)):
            for v4 in range(v3 + 2, a1 + 1):
                v1[v3][v4] = min((k + 1 + max(v1[v3][k], v1[k + 1][v4]) for v5 in range(v3, v4)))
        return v1[0][a1]
