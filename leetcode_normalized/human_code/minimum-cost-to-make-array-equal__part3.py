class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])
        v2 = [0] * (len(a2) + 1)
        v3 = 0
        for v4 in range(len(a2)):
            if v4 - 1 >= 0:
                v3 += v2[v4] * (a1[v1[v4]] - a1[v1[v4 - 1]])
            v2[v4 + 1] = v2[v4] + a2[v1[v4]]
        v5 = float('inf')
        v6 = v7 = 0
        for v4 in reversed(range(len(a2))):
            if v4 + 1 < len(v1):
                v7 += v6 * (a1[v1[v4 + 1]] - a1[v1[v4]])
            v5 = min(v5, v3 + v7)
            if v4 - 1 >= 0:
                v3 -= v2[v4] * (a1[v1[v4]] - a1[v1[v4 - 1]])
            v6 += a2[v1[v4]]
        return v5
