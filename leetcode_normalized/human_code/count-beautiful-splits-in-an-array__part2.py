class C1(object):

    def beautifulSplits(self, a1):
        """
        """
        v1 = [[0] * len(a1) for v2 in range(len(a1))]
        for v3 in reversed(range(len(a1))):
            for v4 in range(v3 + 1, len(v1)):
                v1[v3][v4] = 1 + (v1[v3 + 1][v4 + 1] if v4 + 1 < len(a1) else 0) if a1[v3] == a1[v4] else 0
        v5 = 0
        for v3 in range(1, len(a1) - 1):
            for v4 in range(v3 + 1, len(a1)):
                if v1[0][v3] >= v3 and v4 - v3 >= v3 or v1[v3][v4] >= v4 - v3:
                    v5 += 1
        return v5
