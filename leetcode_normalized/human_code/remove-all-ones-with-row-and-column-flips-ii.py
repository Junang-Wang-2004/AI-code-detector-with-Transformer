class C1(object):

    def removeOnes(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2, v3 = (0, 1)
        for v4 in range(len(a1[0])):
            v2 += v3
            v3 <<= 1
        for v5 in range(len(a1)):
            v1[v5] = v2
            v2 <<= len(a1[0])
        v6 = [0] * len(a1[0])
        v2, v3 = (0, 1)
        for v4 in range(len(a1)):
            v2 += v3
            v3 <<= len(a1[0])
        for v7 in range(len(a1[0])):
            v6[v7] = v2
            v2 <<= 1
        v8 = (1 << len(a1) * len(a1[0])) - 1
        v9 = [[v8 for v4 in range(len(a1[0]))] for v4 in range(len(a1))]
        v10, v3 = (0, 1)
        for v5 in range(len(a1)):
            for v7 in range(len(a1[0])):
                v10 += v3 * a1[v5][v7]
                v9[v5][v7] -= v1[v5] + v6[v7] - v3
                v3 <<= 1
        v11 = [float('inf') for v4 in range(v10 + 1)]
        v11[0] = 0
        for v2 in range(1, v10 + 1):
            for v5 in range(len(a1)):
                for v7 in range(len(a1[0])):
                    if a1[v5][v7]:
                        v11[v2] = min(v11[v2], v11[v2 & v9[v5][v7]] + 1)
        return v11[v10]
