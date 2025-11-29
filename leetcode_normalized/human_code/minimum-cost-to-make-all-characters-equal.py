class C1(object):

    def minimumCost(self, a1):
        """
        """
        return sum((min(i + 1, len(a1) - (i + 1)) for v1 in range(len(a1) - 1) if a1[v1] != a1[v1 + 1]))
