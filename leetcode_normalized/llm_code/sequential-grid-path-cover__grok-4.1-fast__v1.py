class C1:

    def findPath(self, a1, a2):
        if not a1 or not a1[0]:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 * v2
        v4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(a1, a2, a3, a4, a5):
            v1 = a1[a1][a2]
            if v1 != 0 and v1 != a3:
                return False
            a4.append([a1, a2])
            a5[a1][a2] = True
            if len(a4) == v3:
                return True
            v2 = a3 + 1 if v1 == a3 else a3
            for v3, v4 in v4:
                v5, v6 = (a1 + v3, a2 + v4)
                if 0 <= v5 < v1 and 0 <= v6 < v2 and (not a5[v5][v6]):
                    if dfs(v5, v6, v2, a4, a5):
                        return True
            a4.pop()
            a5[a1][a2] = False
            return False
        for v5 in range(v1):
            for v6 in range(v2):
                v7 = [[False] * v2 for v8 in range(v1)]
                v9 = []
                if dfs(v5, v6, 1, v9, v7):
                    return v9
        return []
