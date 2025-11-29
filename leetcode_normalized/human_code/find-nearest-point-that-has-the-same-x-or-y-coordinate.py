class C1(object):

    def nearestValidPoint(self, a1, a2, a3):
        """
        """
        v1, v2 = (float('inf'), -1)
        for v3, (v4, v5) in enumerate(a3):
            v6, v7 = (a1 - v4, a2 - v5)
            if v6 * v7 == 0 and abs(v6) + abs(v7) < v1:
                v1 = abs(v6) + abs(v7)
                v2 = v3
        return v2
