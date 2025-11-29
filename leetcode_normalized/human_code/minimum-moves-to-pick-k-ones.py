class C1(object):

    def minimumMoves(self, a1, a2, a3):
        """
        """
        v1 = [i for v2, v3 in enumerate(a1) if v3]
        v4 = [0] * (len(v1) + 1)
        for v2 in range(len(v1)):
            v4[v2 + 1] = v4[v2] + v1[v2]
        v5 = float('inf')
        v6 = max(a2 - a3, 0)
        for v7 in range(v6, min(v6 + 3, a2, len(v1)) + 1):
            v8 = (a2 - v7) * 2
            for v2 in range(len(v1) - v7 + 1):
                v9 = v4[v2 + v7 - 1 + 1] - v4[v2 + v7 - 1 - (v7 // 2 - 1)] - (v4[v2 + (v7 // 2 - 1) + 1] - v4[v2])
                v5 = min(v5, v9 + v8)
        return v5
