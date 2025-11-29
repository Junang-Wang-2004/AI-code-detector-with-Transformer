class C1(object):

    def countCornerRectangles(self, a1):
        """
        """
        v1 = [[c for v2, v3 in enumerate(row) if v3] for v4 in a1]
        v5 = 0
        for v6 in range(len(v1)):
            v7 = set(v1[v6])
            for v8 in range(v6):
                v9 = sum((1 for v2 in v1[v8] if v2 in v7))
                v5 += v9 * (v9 - 1) / 2
        return v5
