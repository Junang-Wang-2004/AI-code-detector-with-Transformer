class C1(object):

    def champagneTower(self, a1, a2, a3):
        """
        """
        v1 = [a1] + [0] * a2
        for v2 in range(1, a2 + 1):
            for v3 in reversed(range(v2 + 1)):
                v1[v3] = max(v1[v3] - 1, 0) / 2.0 + max(v1[v3 - 1] - 1, 0) / 2.0
        return min(v1[a3], 1)
