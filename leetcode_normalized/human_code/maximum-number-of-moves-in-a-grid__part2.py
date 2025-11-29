class C1(object):

    def maxMoves(self, a1):
        """
        """
        v1 = [0] * len(a1)
        for v2 in reversed(range(len(a1[0]) - 1)):
            v3 = [0] * len(a1)
            for v4 in range(len(a1)):
                if a1[v4][v2] < a1[v4][v2 + 1]:
                    v3[v4] = max(v3[v4], v1[v4] + 1)
                if v4 - 1 >= 0 and a1[v4][v2] < a1[v4 - 1][v2 + 1]:
                    v3[v4] = max(v3[v4], v1[v4 - 1] + 1)
                if v4 + 1 < len(a1) and a1[v4][v2] < a1[v4 + 1][v2 + 1]:
                    v3[v4] = max(v3[v4], v1[v4 + 1] + 1)
            v1 = v3
        return max(v1)
