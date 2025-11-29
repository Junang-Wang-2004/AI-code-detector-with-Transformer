class C1(object):

    def imageSmoother(self, a1):
        """
        """

        def getGray(a1, a2, a3):
            v1, v2 = (0, 0.0)
            for v3 in range(-1, 2):
                for v4 in range(-1, 2):
                    v5, v6 = (a2 + v3, a3 + v4)
                    if 0 <= v5 < len(a1) and 0 <= v6 < len(a1[0]):
                        v1 += a1[v5][v6]
                        v2 += 1.0
            return int(v1 / v2)
        v1 = [[0 for v2 in range(len(a1[0]))] for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v1[v3][v4] = getGray(a1, v3, v4)
        return v1
