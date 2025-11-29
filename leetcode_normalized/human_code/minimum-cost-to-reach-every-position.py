class C1(object):

    def minCosts(self, a1):
        """
        """
        for v1 in range(1, len(a1)):
            a1[v1] = min(a1[v1], a1[v1 - 1])
        return a1
