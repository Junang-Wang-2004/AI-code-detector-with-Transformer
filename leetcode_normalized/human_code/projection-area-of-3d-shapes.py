class C1(object):

    def projectionArea(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3, v4 = (0, 0)
            for v5 in range(len(a1)):
                if a1[v2][v5]:
                    v1 += 1
                v3 = max(v3, a1[v2][v5])
                v4 = max(v4, a1[v5][v2])
            v1 += v3 + v4
        return v1
