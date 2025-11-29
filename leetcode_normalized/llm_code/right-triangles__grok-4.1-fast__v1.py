class C1(object):

    def numberOfRightTriangles(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [sum(a1[r]) for v4 in range(v1)]
        v5 = [sum((a1[v4][c] for v4 in range(v1))) for v6 in range(v2)]
        v7 = 0
        for v4 in range(v1):
            for v6 in range(v2):
                if a1[v4][v6]:
                    v7 += (v3[v4] - 1) * (v5[v6] - 1)
        return v7
