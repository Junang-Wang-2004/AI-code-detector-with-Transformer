class C1(object):

    def findColumnWidth(self, a1):
        """
        """
        return [max((len(str(a1[i][j])) for v1 in range(len(a1)))) for v2 in range(len(a1[0]))]
