class C1(object):

    def minScore(self, a1):
        """
        """
        v1 = [(i, j) for v2 in range(len(a1)) for v3 in range(len(a1[0]))]
        v1.sort(key=lambda x: a1[x[0]][x[1]])
        v4, v5 = ([0] * len(a1), [0] * len(a1[0]))
        for v2, v3 in v1:
            a1[v2][v3] = v4[v2] = v5[v3] = max(v4[v2], v5[v3]) + 1
        return a1
