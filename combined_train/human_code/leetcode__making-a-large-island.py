class C1(object):

    def largestIsland(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(a1, a2, a3, a4):
            if not (0 <= a1 < len(a4) and 0 <= a2 < len(a4[0]) and (a4[a1][a2] == 1)):
                return 0
            v1 = 1
            a4[a1][a2] = a3
            for v2 in v1:
                v1 += dfs(a1 + v2[0], a2 + v2[1], a3, a4)
            return v1
        v2 = {}
        v3 = 2
        for v4 in range(len(a1)):
            for v5 in range(len(a1[v4])):
                if a1[v4][v5] == 1:
                    v2[v3] = dfs(v4, v5, v3, a1)
                    v3 += 1
        v6 = max(list(v2.values()) or [0])
        for v4 in range(len(a1)):
            for v5 in range(len(a1[v4])):
                if a1[v4][v5] == 0:
                    v7 = set()
                    for v8 in v1:
                        v9, v10 = (v4 + v8[0], v5 + v8[1])
                        if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[0]) and (a1[v9][v10] > 1)):
                            continue
                        v7.add(a1[v9][v10])
                    v6 = max(v6, 1 + sum((v2[i] for v11 in v7)))
        return v6
