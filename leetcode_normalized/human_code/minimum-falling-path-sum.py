class C1(object):

    def minFallingPathSum(self, a1):
        """
        """
        for v1 in range(1, len(a1)):
            for v2 in range(len(a1[v1])):
                a1[v1][v2] += min(a1[v1 - 1][max(v2 - 1, 0):v2 + 2])
        return min(a1[-1])
