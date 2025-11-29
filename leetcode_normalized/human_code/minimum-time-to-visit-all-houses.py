class C1(object):

    def minTotalTime(self, a1, a2, a3):
        """
        """
        v1 = [0] * (2 * len(a1) - 1 + 1)
        for v2 in range(2 * len(a1) - 1):
            v1[v2 + 1] = v1[v2] + a1[v2 % len(a1)]
        v3 = [0] * (2 * len(a2) - 1 + 1)
        for v2 in range(2 * len(a2) - 1):
            v3[v2 + 1] = v3[v2] + a2[v2 % len(a2)]
        v4 = v5 = 0
        for v6 in a3:
            if v5 > v6:
                v4 += min(v1[v6 + len(a1)] - v1[v5], v3[v5 + 1] - v3[v6 + 1])
            else:
                v4 += min(v1[v6] - v1[v5], v3[v5 + len(a1) + 1] - v3[v6 + 1])
            v5 = v6
        return v4
