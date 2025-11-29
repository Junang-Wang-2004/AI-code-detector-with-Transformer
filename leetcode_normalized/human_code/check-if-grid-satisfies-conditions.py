class C1(object):

    def satisfiesConditions(self, a1):
        """
        """
        return all((a1[i][j] == a1[i + 1][j] for v1 in range(len(a1[0])) for v2 in range(len(a1) - 1))) and all((a1[0][v1] != a1[0][v1 + 1] for v1 in range(len(a1[0]) - 1)))
