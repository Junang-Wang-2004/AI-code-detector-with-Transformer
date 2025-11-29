class C1:

    def minSideJumps(self, a1):
        v1, v2, v3 = (1, 0, 1)
        for v4 in a1:
            if v4 == 1:
                v1 = float('inf')
            if v4 == 2:
                v2 = float('inf')
            if v4 == 3:
                v3 = float('inf')
            v5 = min(v1, v2 + 1, v3 + 1) if v4 != 1 else float('inf')
            v6 = min(v1 + 1, v2, v3 + 1) if v4 != 2 else float('inf')
            v7 = min(v1 + 1, v2 + 1, v3) if v4 != 3 else float('inf')
            v1, v2, v3 = (v5, v6, v7)
        return min(v1, v2, v3)
