class C1(object):

    def rangeAddQueries(self, a1, a2):
        """
        """
        v1 = [[0] * a1 for v2 in range(a1)]
        for v3, v4, v5, v6 in a2:
            v1[v3][v4] += 1
            if v6 + 1 < len(v1[0]):
                v1[v3][v6 + 1] -= 1
            if v5 + 1 < len(v1):
                v1[v5 + 1][v4] -= 1
            if v5 + 1 < len(v1) and v6 + 1 < len(v1[0]):
                v1[v5 + 1][v6 + 1] += 1
        for v7 in range(len(v1)):
            for v8 in range(len(v1[0]) - 1):
                v1[v7][v8 + 1] += v1[v7][v8]
        for v7 in range(len(v1) - 1):
            for v8 in range(len(v1[0])):
                v1[v7 + 1][v8] += v1[v7][v8]
        return v1
