class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            if v4 and a1[v4] != a1[v4 - 1]:
                v1 += v2 - v3
                v2 = v3 = 0
            v2 += a2[v4]
            v3 = max(v3, a2[v4])
        v1 += v2 - v3
        return v1
