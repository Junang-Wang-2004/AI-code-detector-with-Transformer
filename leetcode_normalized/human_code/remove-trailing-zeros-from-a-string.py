class C1(object):

    def removeTrailingZeros(self, a1):
        """
        """
        return a1[:next((i for v1 in reversed(range(len(a1))) if a1[v1] != '0')) + 1]
