class C1(object):

    def checkXMatrix(self, a1):
        """
        """
        return all(((i - j == 0 or i + j == len(a1) - 1) == (a1[i][j] != 0) for v1 in range(len(a1)) for v2 in range(len(a1[0]))))
