class C1(object):

    def numberOfRightTriangles(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [sum((a1[i][j] for v4 in range(v2))) for v5 in range(v1)]
        v6 = [sum((a1[v5][v4] for v5 in range(v1))) for v4 in range(v2)]
        return sum(((v3[v5] - 1) * (v6[v4] - 1) for v5 in range(v1) for v4 in range(v2) if a1[v5][v4]))
