class C1(object):

    def findArray(self, a1):
        """
        """
        for v1 in reversed(range(1, len(a1))):
            a1[v1] ^= a1[v1 - 1]
        return a1
