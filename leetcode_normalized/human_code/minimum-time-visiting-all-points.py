class C1(object):

    def minTimeToVisitAllPoints(self, a1):
        """
        """
        return sum((max(abs(a1[i + 1][0] - a1[i][0]), abs(a1[i + 1][1] - a1[i][1])) for v1 in range(len(a1) - 1)))
