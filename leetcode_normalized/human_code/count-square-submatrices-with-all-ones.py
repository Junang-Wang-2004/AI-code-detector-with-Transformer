class C1(object):

    def countSquares(self, a1):
        """
        """
        for v1 in range(1, len(a1)):
            for v2 in range(1, len(a1[0])):
                if not a1[v1][v2]:
                    continue
                v3 = min(a1[v1 - 1][v2], a1[v1][v2 - 1])
                a1[v1][v2] = v3 + 1 if a1[v1 - v3][v2 - v3] else v3
        return sum((x for v4 in a1 for v5 in v4))
