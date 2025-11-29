class C1(object):

    def minChanges(self, a1, a2):
        """
        """
        v1 = [0] * (a2 + 1 + 1)

        def update(a1, a2, a3):
            v1[a1] += a3
            v1[a2 + 1] -= a3
        for v2 in range(len(a1) // 2):
            v3 = abs(a1[v2] - a1[~v2])
            v4 = max(a1[v2] - 0, a2 - a1[v2], a1[~v2] - 0, a2 - a1[~v2])
            update(0, v3 - 1, 1)
            update(v3 + 1, v4, 1)
            update(v4 + 1, a2, 2)
        v5 = len(a1) // 2
        v3 = 0
        for v2 in range(a2 + 1):
            v3 += v1[v2]
            v5 = min(v5, v3)
        return v5
