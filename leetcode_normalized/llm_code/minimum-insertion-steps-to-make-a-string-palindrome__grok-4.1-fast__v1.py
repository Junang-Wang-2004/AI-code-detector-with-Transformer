class C1(object):

    def minInsertions(self, a1):
        v1 = len(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(v1 - 1):
            v2[v4][v4 + 1] = 0 if a1[v4] == a1[v4 + 1] else 1
        for v5 in range(3, v1 + 1):
            for v6 in range(v1 - v5 + 1):
                v7 = v6 + v5 - 1
                if a1[v6] == a1[v7]:
                    v2[v6][v7] = v2[v6 + 1][v7 - 1]
                else:
                    v2[v6][v7] = 1 + min(v2[v6][v7 - 1], v2[v6 + 1][v7])
        return v2[0][v1 - 1]
