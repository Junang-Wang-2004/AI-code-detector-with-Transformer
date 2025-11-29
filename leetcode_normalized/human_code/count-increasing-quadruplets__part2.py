class C1(object):

    def countQuadruplets(self, a1):
        """
        """
        v1 = [[0] * (len(a1) + 1) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in reversed(range(v3 + 1, len(a1))):
                v1[v3][v4] = v1[v3][v4 + 1] + int(a1[v4] > a1[v3])
        v5 = 0
        for v6 in range(len(a1)):
            v7 = 0
            for v3 in range(v6):
                if a1[v6] < a1[v3]:
                    v5 += v7 * v1[v3][v6 + 1]
                v7 += int(a1[v6] > a1[v3])
        return v5
