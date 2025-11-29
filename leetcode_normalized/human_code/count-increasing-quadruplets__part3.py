class C1(object):

    def countQuadruplets(self, a1):
        """
        """
        v1 = [[0] * (len(a1) + 1) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in range(v3):
                v1[v3][v4 + 1] = v1[v3][v4] + int(a1[v4] < a1[v3])
        v5 = [[0] * (len(a1) + 1) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in reversed(range(v3 + 1, len(a1))):
                v5[v3][v4] = v5[v3][v4 + 1] + int(a1[v4] > a1[v3])
        v6 = 0
        for v7 in range(len(a1)):
            for v3 in range(v7):
                if a1[v7] < a1[v3]:
                    v6 += v1[v7][v3] * v5[v3][v7 + 1]
        return v6
