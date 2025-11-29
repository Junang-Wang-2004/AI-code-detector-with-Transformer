class C1(object):

    def removeOnes(self, a1):
        """
        """
        return all((a1[i] == a1[0] or all((a1[i][j] != a1[0][j] for v1 in range(len(a1[0])))) for v2 in range(1, len(a1))))
