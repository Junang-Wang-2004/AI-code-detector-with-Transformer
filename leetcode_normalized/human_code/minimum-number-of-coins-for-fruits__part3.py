class C1(object):

    def minimumCoins(self, a1):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2 in range(len(a1)):
            for v3 in range(v2 // 2, v2 + 1):
                v1[v2 + 1] = min(v1[v2 + 1], v1[v3] + a1[v3])
        return v1[-1]
