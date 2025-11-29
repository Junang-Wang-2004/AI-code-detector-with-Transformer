class C1(object):

    def closestCost(self, a1, a2, a3):
        """
        """
        v1 = 2
        v2 = set([0])
        for v3 in a2:
            v2 = set([c + i * v3 for v4 in v2 for v5 in range(v1 + 1)])
        v6 = float('inf')
        for v7 in a1:
            for v4 in v2:
                v6 = min(v6, v7 + v4, key=lambda x: (abs(x - a3), x))
        return v6
