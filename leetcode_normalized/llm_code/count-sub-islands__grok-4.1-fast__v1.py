class C1:

    def countSubIslands(self, a1, a2):
        if not a2 or not a2[0]:
            return 0
        v1, v2 = (len(a2), len(a2[0]))
        v3 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def erase(a1, a2):
            if a1 < 0 or a1 >= v1 or a2 < 0 or (a2 >= v2) or (a2[a1][a2] != 1):
                return
            a2[a1][a2] = 0
            for v1, v2 in v3:
                erase(a1 + v1, a2 + v2)
        for v4 in range(v1):
            for v5 in range(v2):
                if a2[v4][v5] == 1 and a1[v4][v5] == 0:
                    erase(v4, v5)
        v6 = 0
        for v4 in range(v1):
            for v5 in range(v2):
                if a2[v4][v5] == 1:
                    erase(v4, v5)
                    v6 += 1
        return v6
