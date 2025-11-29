class C1(object):

    def maximumProduct(self, a1, a2):
        """
        """
        v1 = v2 = float('-inf')
        v3 = float('inf')
        for v4 in range(len(a1) - (a2 - 1)):
            v2 = max(v2, a1[v4])
            v3 = min(v3, a1[v4])
            v1 = max(v1, a1[v4 + (a2 - 1)] * v2, a1[v4 + (a2 - 1)] * v3)
        return v1
