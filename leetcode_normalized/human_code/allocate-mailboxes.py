class C1(object):

    def minDistance(self, a1, a2):
        """
        """

        def cost(a1, a2, a3):
            return a1[a3 + 1] - a1[(a2 + a3 + 1) // 2] - (a1[(a2 + a3) // 2 + 1] - a1[a2])
        a1.sort()
        v1 = [0] * (len(a1) + 1)
        for v2, v3 in enumerate(a1):
            v1[v2 + 1] = v1[v2] + v3
        v4 = [cost(v1, 0, j) for v5 in range(len(a1))]
        for v6 in range(1, a2):
            for v5 in reversed(range(v6, len(a1))):
                for v2 in range(v6, v5 + 1):
                    v4[v5] = min(v4[v5], v4[v2 - 1] + cost(v1, v2, v5))
        return v4[-1]
