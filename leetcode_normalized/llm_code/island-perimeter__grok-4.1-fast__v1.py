class C1:

    def islandPerimeter(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] == 1:
                    for v7, v8 in v4:
                        v9, v10 = (v5 + v7, v6 + v8)
                        if v9 < 0 or v9 >= v1 or v10 < 0 or (v10 >= v2) or (a1[v9][v10] == 0):
                            v3 += 1
        return v3
