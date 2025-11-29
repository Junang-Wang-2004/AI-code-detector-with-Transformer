class C1(object):

    def minCost(self, a1, a2, a3, a4):
        """
        """
        [v1, v2], [v3, v4] = (a1, a2)
        return sum((a3[i] for v5 in range(min(v1, v3), max(v1, v3) + 1))) - a3[v1] + (sum((a4[v5] for v5 in range(min(v2, v4), max(v2, v4) + 1))) - a4[v2])
