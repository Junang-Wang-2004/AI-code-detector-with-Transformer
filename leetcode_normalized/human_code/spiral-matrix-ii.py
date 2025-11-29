class C1(object):

    def generateMatrix(self, a1):
        v1 = [[0 for v2 in range(a1)] for v2 in range(a1)]
        v3, v4, v5, v6, v7 = (0, a1 - 1, 0, a1 - 1, 1)
        while v3 <= v4 and v5 <= v6:
            for v8 in range(v3, v4 + 1):
                v1[v5][v8] = v7
                v7 += 1
            for v9 in range(v5 + 1, v6):
                v1[v9][v4] = v7
                v7 += 1
            for v8 in reversed(range(v3, v4 + 1)):
                if v5 < v6:
                    v1[v6][v8] = v7
                    v7 += 1
            for v9 in reversed(range(v5 + 1, v6)):
                if v3 < v4:
                    v1[v9][v3] = v7
                    v7 += 1
            v3, v4, v5, v6 = (v3 + 1, v4 - 1, v5 + 1, v6 - 1)
        return v1
