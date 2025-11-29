class C1(object):

    def minIncrementOperations(self, a1, a2):
        """
        """
        v1 = 3
        v2 = [0] * v1
        for v3, v4 in enumerate(a1):
            v2[v3 % v1] = min((v2[j % v1] for v5 in range(v3 - v1, v3))) + max(a2 - v4, 0)
        return min(v2)
