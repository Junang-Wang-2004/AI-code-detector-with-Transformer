class C1(object):

    def longestIncreasingPath(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def longestpath(a1, a2, a3, a4):
            if a4[a2][a3]:
                return a4[a2][a3]
            v1 = 0
            for v2, v3 in v1:
                v4, v5 = (a2 + v2, a3 + v3)
                if 0 <= v4 < len(a1) and 0 <= v5 < len(a1[0]) and (a1[v4][v5] < a1[a2][a3]):
                    v1 = max(v1, longestpath(a1, v4, v5, a4))
            a4[a2][a3] = v1 + 1
            return a4[a2][a3]
        if not a1:
            return 0
        v2 = 0
        v3 = [[0 for v4 in range(len(a1[0]))] for v4 in range(len(a1))]
        for v5 in range(len(a1)):
            for v6 in range(len(a1[0])):
                v2 = max(v2, longestpath(a1, v5, v6, v3))
        return v2
