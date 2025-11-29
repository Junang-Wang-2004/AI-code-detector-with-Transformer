class C1(object):

    def maximumTotalCost(self, a1):
        """
        """
        v1 = [a1[0], float('-inf')]
        for v2 in range(1, len(a1)):
            v1[:] = [max(v1) + a1[v2], v1[0] - a1[v2]]
        return max(v1)
