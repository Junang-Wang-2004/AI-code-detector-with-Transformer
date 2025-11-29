class C1(object):

    def largestSumOfAverages(self, a1, a2):
        v1 = len(a1)
        v2 = [0.0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [[0.0] * v1 for v5 in range(a2 + 1)]
        for v3 in range(v1):
            v4[1][v3] = v2[v3 + 1] / (v3 + 1)
        for v6 in range(2, a2 + 1):
            for v3 in range(v6 - 1, v1):
                v4[v6][v3] = max((v4[v6 - 1][j] + (v2[v3 + 1] - v2[j + 1]) / (v3 - j) for v7 in range(v6 - 2, v3)))
        return v4[a2][v1 - 1]
