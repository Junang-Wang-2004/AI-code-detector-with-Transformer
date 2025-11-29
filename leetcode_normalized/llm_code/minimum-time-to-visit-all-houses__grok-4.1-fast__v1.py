class C1(object):

    def minTotalTime(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [0] * (2 * v1 + 1)
        for v3 in range(2 * v1):
            v2[v3 + 1] = v2[v3] + a1[v3 % v1]
        v4 = [0] * (2 * v1 + 1)
        for v3 in range(2 * v1):
            v4[v3 + 1] = v4[v3] + a2[v3 % v1]
        v5 = 0
        v6 = 0
        for v7 in a3:
            v8 = v2[v7 + v1 if v7 < v6 else v7] - v2[v6]
            v9 = v4[v6 + v1 + 1 if v6 < v7 else v6 + 1] - v4[v7 + 1]
            v5 += min(v8, v9)
            v6 = v7
        return v5
