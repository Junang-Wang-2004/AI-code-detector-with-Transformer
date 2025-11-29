class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = [a2 * k for v2 in range(len(a1) + 1)]
        for v3 in range(len(a1)):
            v4 = a1[v3]
            for v2 in range(len(v1)):
                v4 = min(v4, a1[(v3 + v2) % len(a1)])
                v1[v2] += v4
        return min(v1)
