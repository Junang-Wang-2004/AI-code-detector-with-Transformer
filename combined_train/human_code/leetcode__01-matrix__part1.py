class C1(object):

    def updateMatrix(self, a1):
        """
        """
        for v1 in range(len(a1)):
            for v2 in range(len(a1[v1])):
                if not a1[v1][v2]:
                    continue
                a1[v1][v2] = float('inf')
                if v1 > 0:
                    a1[v1][v2] = min(a1[v1][v2], a1[v1 - 1][v2] + 1)
                if v2 > 0:
                    a1[v1][v2] = min(a1[v1][v2], a1[v1][v2 - 1] + 1)
        for v1 in reversed(range(len(a1))):
            for v2 in reversed(range(len(a1[v1]))):
                if not a1[v1][v2]:
                    continue
                if v1 < len(a1) - 1:
                    a1[v1][v2] = min(a1[v1][v2], a1[v1 + 1][v2] + 1)
                if v2 < len(a1[v1]) - 1:
                    a1[v1][v2] = min(a1[v1][v2], a1[v1][v2 + 1] + 1)
        return a1
