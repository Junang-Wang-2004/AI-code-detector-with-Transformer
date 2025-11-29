class C1(object):

    def sortedSquares(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3, v4 = (0, v1 - 1)
        for v5 in range(v1 - 1, -1, -1):
            if a1[v3] ** 2 > a1[v4] ** 2:
                v2[v5] = a1[v3] ** 2
                v3 += 1
            else:
                v2[v5] = a1[v4] ** 2
                v4 -= 1
        return v2
