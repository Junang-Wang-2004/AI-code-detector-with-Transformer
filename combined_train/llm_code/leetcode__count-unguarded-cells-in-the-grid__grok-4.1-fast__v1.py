class C1(object):

    def countUnguarded(self, a1, a2, a3, a4):
        v1 = [[0] * a2 for v2 in range(a1)]
        for v3, v4 in a3:
            v1[v3][v4] = 2
        for v3, v4 in a4:
            v1[v3][v4] = 1
        for v5 in range(a1):
            v6 = False
            for v7 in range(a2):
                if v1[v5][v7] == 1 or v1[v5][v7] == 2:
                    v6 = v1[v5][v7] == 2
                elif v1[v5][v7] == 0 and v6:
                    v1[v5][v7] = 3
            v6 = False
            for v7 in range(a2 - 1, -1, -1):
                if v1[v5][v7] == 1 or v1[v5][v7] == 2:
                    v6 = v1[v5][v7] == 2
                elif v1[v5][v7] == 0 and v6:
                    v1[v5][v7] = 3
        for v7 in range(a2):
            v6 = False
            for v5 in range(a1):
                if v1[v5][v7] == 1 or v1[v5][v7] == 2:
                    v6 = v1[v5][v7] == 2
                elif v1[v5][v7] == 0 and v6:
                    v1[v5][v7] = 3
            v6 = False
            for v5 in range(a1 - 1, -1, -1):
                if v1[v5][v7] == 1 or v1[v5][v7] == 2:
                    v6 = v1[v5][v7] == 2
                elif v1[v5][v7] == 0 and v6:
                    v1[v5][v7] = 3
        return sum((row.count(0) for v8 in v1))
