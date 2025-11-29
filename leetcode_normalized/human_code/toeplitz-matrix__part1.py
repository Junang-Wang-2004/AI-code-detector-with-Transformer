class C1(object):

    def isToeplitzMatrix(self, a1):
        """
        """
        return all((i == 0 or j == 0 or a1[i - 1][j - 1] == val for v1, v2 in enumerate(a1) for v3, v4 in enumerate(v2)))
