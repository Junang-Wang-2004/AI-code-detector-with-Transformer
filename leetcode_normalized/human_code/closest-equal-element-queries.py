class C1(object):

    def solveQueries(self, a1, a2):
        """
        """
        v1 = [len(a1)] * len(a1)
        v2 = {}
        for v3 in range(2 * len(a1) - 1):
            v4 = a1[v3 % len(a1)]
            if v4 in v2:
                v1[v3 % len(v1)] = min(v1[v3 % len(v1)], v3 - v2[v4])
            v2[v4] = v3
        v5 = {}
        for v3 in reversed(range(2 * len(a1) - 1)):
            v4 = a1[v3 % len(a1)]
            if v4 in v5:
                v1[v3 % len(v1)] = min(v1[v3 % len(v1)], v5[v4] - v3)
            v5[v4] = v3
        v6 = [-1] * len(a2)
        for v3, v4 in enumerate(a2):
            if v1[v4] < len(a1):
                v6[v3] = v1[v4]
        return v6
