class C1(object):

    def deleteGreatestValue(self, a1):
        """
        """
        for v1 in a1:
            v1.sort()
        return sum((max((a1[i][j] for v2 in range(len(a1)))) for v3 in range(len(a1[0]))))
