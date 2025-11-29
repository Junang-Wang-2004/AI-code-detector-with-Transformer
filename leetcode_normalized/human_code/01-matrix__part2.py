class C1(object):

    def updateMatrix(self, a1):
        """
        """
        v1 = [[float('inf')] * len(a1[0]) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in range(len(a1[v3])):
                if a1[v3][v4] == 0:
                    v1[v3][v4] = 0
                else:
                    if v3 > 0:
                        v1[v3][v4] = min(v1[v3][v4], v1[v3 - 1][v4] + 1)
                    if v4 > 0:
                        v1[v3][v4] = min(v1[v3][v4], v1[v3][v4 - 1] + 1)
        for v3 in reversed(range(len(a1))):
            for v4 in reversed(range(len(a1[v3]))):
                if a1[v3][v4] == 0:
                    v1[v3][v4] = 0
                else:
                    if v3 < len(a1) - 1:
                        v1[v3][v4] = min(v1[v3][v4], v1[v3 + 1][v4] + 1)
                    if v4 < len(a1[v3]) - 1:
                        v1[v3][v4] = min(v1[v3][v4], v1[v3][v4 + 1] + 1)
        return v1
