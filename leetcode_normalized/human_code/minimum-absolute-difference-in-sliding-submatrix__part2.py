class C1(object):

    def minAbsDiff(self, a1, a2):
        """
        """
        v1 = [[-1] * (len(a1[0]) - (a2 - 1)) for v2 in range(len(a1) - (a2 - 1))]
        for v3 in range(len(a1) - (a2 - 1)):
            for v4 in range(len(a1[0]) - (a2 - 1)):
                v5 = sorted({a1[v3 + di][v4 + dj] for v6 in range(a2) for v7 in range(a2)})
                v1[v3][v4] = min((v5[x + 1] - v5[x] for v8 in range(len(v5) - 1))) if len(v5) != 1 else 0
        return v1
