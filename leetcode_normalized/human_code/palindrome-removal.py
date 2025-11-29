class C1(object):

    def minimumMoves(self, a1):
        """
        """
        v1 = [[0 for v2 in range(len(a1) + 1)] for v2 in range(len(a1) + 1)]
        for v3 in range(1, len(a1) + 1):
            for v4 in range(len(a1) - v3 + 1):
                v5 = v4 + v3 - 1
                if v3 == 1:
                    v1[v4][v5] = 1
                else:
                    v1[v4][v5] = 1 + v1[v4 + 1][v5]
                    if a1[v4] == a1[v4 + 1]:
                        v1[v4][v5] = min(v1[v4][v5], 1 + v1[v4 + 2][v5])
                    for v6 in range(v4 + 2, v5 + 1):
                        if a1[v4] == a1[v6]:
                            v1[v4][v5] = min(v1[v4][v5], v1[v4 + 1][v6 - 1] + v1[v6 + 1][v5])
        return v1[0][len(a1) - 1]
