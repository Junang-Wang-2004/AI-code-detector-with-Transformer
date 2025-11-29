class C1:

    def maxAreaOfIsland(self, a1):
        if not a1:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = 0

        def flood(a1, a2):
            if a1 < 0 or a1 >= v1 or a2 < 0 or (a2 >= v2) or (a1[a1][a2] != 1):
                return 0
            a1[a1][a2] = 0
            return 1 + flood(a1 - 1, a2) + flood(a1 + 1, a2) + flood(a1, a2 - 1) + flood(a1, a2 + 1)
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] == 1:
                    v3 = max(v3, flood(v4, v5))
        return v3
