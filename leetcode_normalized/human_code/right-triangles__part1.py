class C1(object):

    def numberOfRightTriangles(self, a1):
        """
        """

        def get(a1, a2):
            return a1[a1][a2] if n < m else a1[a2][a1]
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4 = [sum((get(i, j) for v5 in range(max(v1, v2)))) for v6 in range(min(v1, v2))]
        for v5 in range(max(v1, v2)):
            v7 = sum((get(v6, v5) for v6 in range(min(v1, v2))))
            v3 += sum(((v4[v6] - 1) * (v7 - 1) for v6 in range(min(v1, v2)) if get(v6, v5)))
        return v3
