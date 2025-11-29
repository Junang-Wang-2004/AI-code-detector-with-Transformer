class C1(object):

    def minDifficulty(self, a1, a2):
        """
        """
        if len(a1) < a2:
            return -1
        v1 = [[float('inf')] * len(a1) for v2 in range(a2)]
        v1[0][0] = a1[0]
        for v3 in range(1, len(a1)):
            v1[0][v3] = max(v1[0][v3 - 1], a1[v3])
        for v3 in range(1, a2):
            for v4 in range(v3, len(a1)):
                v5 = a1[v4]
                for v6 in reversed(range(v3, v4 + 1)):
                    v5 = max(v5, a1[v6])
                    v1[v3][v4] = min(v1[v3][v4], v1[v3 - 1][v6 - 1] + v5)
        return v1[a2 - 1][len(a1) - 1]
