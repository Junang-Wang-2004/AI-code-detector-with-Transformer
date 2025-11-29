class C1(object):

    def findDiagonalOrder(self, a1):
        """
        """
        if not a1 or not a1[0]:
            return []
        v1 = []
        v2, v3, v4 = (0, 0, 0)
        v5 = [(-1, 1), (1, -1)]
        for v6 in range(len(a1) * len(a1[0])):
            v1.append(a1[v2][v3])
            v2 += v5[v4][0]
            v3 += v5[v4][1]
            if v2 >= len(a1):
                v2 = len(a1) - 1
                v3 += 2
                v4 = 1 - v4
            elif v3 >= len(a1[0]):
                v3 = len(a1[0]) - 1
                v2 += 2
                v4 = 1 - v4
            elif v2 < 0:
                v2 = 0
                v4 = 1 - v4
            elif v3 < 0:
                v3 = 0
                v4 = 1 - v4
        return v1
