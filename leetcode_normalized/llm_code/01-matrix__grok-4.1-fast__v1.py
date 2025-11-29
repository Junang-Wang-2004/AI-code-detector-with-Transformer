class C1:

    def updateMatrix(self, a1):
        if not a1 or not a1[0]:
            return a1
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 10 ** 9
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] != 0:
                    a1[v4][v5] = v3
        for v4 in range(v1):
            for v5 in range(v2):
                if v4 > 0:
                    a1[v4][v5] = min(a1[v4][v5], a1[v4 - 1][v5] + 1)
                if v5 > 0:
                    a1[v4][v5] = min(a1[v4][v5], a1[v4][v5 - 1] + 1)
        for v4 in range(v1 - 1, -1, -1):
            for v5 in range(v2 - 1, -1, -1):
                if v4 < v1 - 1:
                    a1[v4][v5] = min(a1[v4][v5], a1[v4 + 1][v5] + 1)
                if v5 < v2 - 1:
                    a1[v4][v5] = min(a1[v4][v5], a1[v4][v5 + 1] + 1)
        return a1
