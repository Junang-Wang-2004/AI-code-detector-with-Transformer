class C1(object):

    def maxWeight(self, a1, a2, a3):
        """
        """
        v1 = [[False] * (a3 + 1) for v2 in range(a2 + 1)]
        v1[0][0] = True
        for v3 in a1:
            v1 = [[v1[i][j] or (i - v3 >= 0 and v1[i - v3][j]) or (j - v3 >= 0 and v1[i][j - v3]) for v4 in range(a3 + 1)] for v5 in range(a2 + 1)]
        v6 = 0
        for v5 in range(a2 + 1):
            for v4 in reversed(range(a3 + 1)):
                if v1[v5][v4]:
                    v6 = max(v6, v5 + v4)
                    break
        return v6
