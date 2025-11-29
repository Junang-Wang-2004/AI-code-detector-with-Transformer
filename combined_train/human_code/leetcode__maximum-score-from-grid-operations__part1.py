class C1(object):

    def maximumScore(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2][0]
        v3 = 0
        v4 = [[0] * (len(a1) + 1) for v5 in range(2)]
        for v6 in range(1, len(a1[0])):
            v7 = [0] * (len(a1) + 1)
            for v2 in range(len(a1)):
                v7[v2 + 1] = v7[v2] + a1[v2][v6]
            v8 = [[0] * (len(a1) + 1) for v5 in range(2)]
            for v2 in range(len(a1) + 1):
                for v9 in range(v2 + 1):
                    v8[0][v2] = max(v8[0][v2], v1[v2] - v1[v9] + v4[0][v9])
                v8[0][v2] = max(v8[0][v2], max(v4[1]))
                for v9 in range(v2 + 1, len(a1) + 1):
                    v8[1][v2] = max(v8[1][v2], v4[1][v9] + (v7[v9] - v7[v2]))
                v8[1][v2] = max(v8[1][v2], v8[0][v2])
            v4, v1 = (v8, v7)
        return max(v4[1])
