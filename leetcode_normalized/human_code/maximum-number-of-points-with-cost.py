class C1(object):

    def maxPoints(self, a1):
        """
        """
        v1 = a1[0]
        for v2 in range(1, len(a1)):
            v3 = [0] * len(a1[v2])
            v3[0] = v1[0]
            for v4 in range(1, len(a1[v2])):
                v3[v4] = max(v3[v4 - 1], v1[v4] + v4)
            v5 = [0] * len(a1[v2])
            v5[-1] = v1[-1] - (len(a1[v2]) - 1)
            for v4 in reversed(range(len(a1[v2]) - 1)):
                v5[v4] = max(v5[v4 + 1], v1[v4] - v4)
            v6 = [0] * len(a1[v2])
            for v4 in range(len(a1[v2])):
                v6[v4] = max(v3[v4] - v4, v5[v4] + v4) + a1[v2][v4]
            v1 = v6
        return max(v1)
