class C1(object):

    def minimumTime(self, a1, a2, a3):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2, (v3, v4) in enumerate(sorted(zip(a2, a1)), 1):
            for v5 in reversed(range(1, v2 + 1)):
                v1[v5] = max(v1[v5], v1[v5 - 1] + (v4 + v5 * v3))
        v6, v7 = (sum(a1), sum(a2))
        return next((v5 for v5 in range(len(v1)) if v6 + v5 * v7 - v1[v5] <= a3), -1)
