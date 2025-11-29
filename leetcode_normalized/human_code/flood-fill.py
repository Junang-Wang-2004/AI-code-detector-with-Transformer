class C1(object):

    def floodFill(self, a1, a2, a3, a4):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(a1, a2, a3, a4, a5):
            if not (0 <= a2 < len(a1) and 0 <= a3 < len(a1[0]) and (a1[a2][a3] == a5)):
                return
            a1[a2][a3] = a4
            for v1 in v1:
                dfs(a1, a2 + v1[0], a3 + v1[1], a4, a5)
        v2 = a1[a2][a3]
        if v2 == a4:
            return a1
        dfs(a1, a2, a3, a4, v2)
        return a1
