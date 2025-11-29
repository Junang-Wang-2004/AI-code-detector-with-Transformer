class C1(object):

    def maximumScore(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2][0]
        v3 = [[0] * (len(a1) + 1) for v4 in range(2)]
        for v5 in range(1, len(a1[0])):
            v6 = [0] * (len(a1) + 1)
            for v2 in range(len(a1)):
                v6[v2 + 1] = v6[v2] + a1[v2][v5]
            v7 = [[0] * (len(a1) + 1) for v4 in range(2)]
            for v2 in range(len(a1) + 1):
                for v8 in range(len(a1) + 1):
                    v7[0][v2] = max(v7[0][v2], max(v1[v2] - v1[v8], 0) + v3[0][v8])
                    v7[1][v2] = max(v7[1][v2], v3[1][v8] + max(v6[v8] - v6[v2], 0))
                v7[0][v2] = max(v7[0][v2], max(v3[1]))
                v7[1][v2] = max(v7[1][v2], v7[0][v2])
            v3, v1 = (v7, v6)
        return max(v3[1])
