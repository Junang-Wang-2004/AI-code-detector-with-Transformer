class C1:

    def containsCycle(self, a1):
        if not a1:
            return False
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[False] * v2 for v4 in range(v1)]

        def explore(a1, a2, a3, a4):
            v3[a1][a2] = True
            for v1, v2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                v3, v4 = (a1 + v1, a2 + v2)
                if 0 <= v3 < v1 and 0 <= v4 < v2 and (a1[v3][v4] == a1[a1][a2]):
                    if v3 == a3 and v4 == a4:
                        continue
                    if v3[v3][v4]:
                        return True
                    if explore(v3, v4, a1, a2):
                        return True
            return False
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] and (not v3[v5][v6]):
                    if explore(v5, v6, -1, -1):
                        return True
        return False
