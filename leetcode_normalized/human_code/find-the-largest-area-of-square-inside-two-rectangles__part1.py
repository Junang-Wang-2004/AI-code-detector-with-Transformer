class C1(object):

    def largestSquareArea(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            for v3 in range(v2 + 1, len(a1)):
                v4 = max(a1[v2][0], a1[v3][0])
                v5 = min(a2[v2][0], a2[v3][0])
                v6 = max(a1[v2][1], a1[v3][1])
                v7 = min(a2[v2][1], a2[v3][1])
                v1 = max(v1, min(v5 - v4, v7 - v6))
        return v1 ** 2
