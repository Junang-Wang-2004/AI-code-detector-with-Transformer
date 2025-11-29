class C1(object):

    def matrixSumQueries(self, a1, a2):
        """
        """
        v1 = [[False] * a1 for v2 in range(2)]
        v3 = [0] * 2
        v4 = 0
        for v5, v6, v7 in reversed(a2):
            if v1[v5][v6]:
                continue
            v1[v5][v6] = True
            v3[v5] += 1
            v4 += v7 * (a1 - v3[v5 ^ 1])
        return v4
