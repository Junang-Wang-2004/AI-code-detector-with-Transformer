class C1(object):

    def orderOfLargestPlusSign(self, a1, a2):
        """
        """
        v1 = {tuple(mine) for v2 in a2}
        v3 = [[0] * a1 for v4 in range(a1)]
        v5 = 0
        for v6 in range(a1):
            v7 = 0
            for v8 in range(a1):
                v7 = 0 if (v6, v8) in v1 else v7 + 1
                v3[v6][v8] = v7
            v7 = 0
            for v8 in reversed(range(a1)):
                v7 = 0 if (v6, v8) in v1 else v7 + 1
                v3[v6][v8] = min(v3[v6][v8], v7)
        for v8 in range(a1):
            v7 = 0
            for v6 in range(a1):
                v7 = 0 if (v6, v8) in v1 else v7 + 1
                v3[v6][v8] = min(v3[v6][v8], v7)
            v7 = 0
            for v6 in reversed(range(a1)):
                v7 = 0 if (v6, v8) in v1 else v7 + 1
                v3[v6][v8] = min(v3[v6][v8], v7)
                v5 = max(v5, v3[v6][v8])
        return v5
