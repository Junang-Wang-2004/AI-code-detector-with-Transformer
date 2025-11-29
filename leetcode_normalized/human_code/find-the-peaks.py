class C1(object):

    def findPeaks(self, a1):
        """
        """
        return [i for v1 in range(1, len(a1) - 1) if a1[v1 - 1] < a1[v1] > a1[v1 + 1]]
