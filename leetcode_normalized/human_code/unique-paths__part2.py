class C1(object):

    def uniquePaths(self, a1, a2):
        """
        """
        if a1 < a2:
            a1, a2 = (a2, a1)
        v3 = [1] * a2
        for v4 in range(1, a1):
            for v5 in range(1, a2):
                v3[v5] += v3[v5 - 1]
        return v3[a2 - 1]
