class C1(object):

    def maxCoins(self, a1, a2):
        """
        """
        v1 = v2 = v3 = v4 = float('-inf')
        for v5 in range(len(a1)):
            v2 = max(v2, 0) + a1[v5]
            v3 = max(max(v3, 0) + a2[v5], v2)
            v4 = max(max(v4, 0) + a1[v5], v3)
            v1 = max(v1, v2, v4)
        return v1
