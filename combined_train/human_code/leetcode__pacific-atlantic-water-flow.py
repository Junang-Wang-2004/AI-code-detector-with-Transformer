class C1(object):

    def pacificAtlantic(self, a1):
        """
        """
        v1, v2 = (1, 2)

        def pacificAtlanticHelper(a1, a2, a3, a4, a5, a6, a7):
            if not 0 <= a2 < len(a1) or not 0 <= a3 < len(a1[0]) or a1[a2][a3] < a4 or (a6[a2][a3] | a5 == a6[a2][a3]):
                return
            a6[a2][a3] |= a5
            if a6[a2][a3] == v1 | v2:
                a7.append((a2, a3))
            for v1 in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                pacificAtlanticHelper(a1, a2 + v1[0], a3 + v1[1], a1[a2][a3], a6[a2][a3], a6, a7)
        if not a1:
            return []
        v3 = []
        v4, v5 = (len(a1), len(a1[0]))
        v6 = [[0 for v7 in range(v5)] for v7 in range(v4)]
        for v8 in range(v4):
            pacificAtlanticHelper(a1, v8, 0, float('-inf'), v1, v6, v3)
            pacificAtlanticHelper(a1, v8, v5 - 1, float('-inf'), v2, v6, v3)
        for v9 in range(v5):
            pacificAtlanticHelper(a1, 0, v9, float('-inf'), v1, v6, v3)
            pacificAtlanticHelper(a1, v4 - 1, v9, float('-inf'), v2, v6, v3)
        return v3
