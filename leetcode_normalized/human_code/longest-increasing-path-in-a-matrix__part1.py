class C1(object):

    def longestIncreasingPath(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if not a1:
            return 0
        v2 = [[0] * len(a1[0]) for v3 in range(len(a1))]
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                for v6, v7 in v1:
                    v8, v9 = (v4 + v6, v5 + v7)
                    if not (0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and (a1[v8][v9] > a1[v4][v5])):
                        continue
                    v2[v4][v5] += 1
        v10 = []
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                if not v2[v4][v5]:
                    v10.append((v4, v5))
        v11 = 0
        while v10:
            v12 = []
            for v4, v5 in v10:
                for v6, v7 in v1:
                    v8, v9 = (v4 + v6, v5 + v7)
                    if not (0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and (a1[v4][v5] > a1[v8][v9])):
                        continue
                    v2[v8][v9] -= 1
                    if not v2[v8][v9]:
                        v12.append((v8, v9))
            v10 = v12
            v11 += 1
        return v11
