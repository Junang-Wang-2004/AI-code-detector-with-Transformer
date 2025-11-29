class C1(object):

    def getMaximumGold(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtracking(a1, a2, a3):
            v1 = 0
            a1[a2][a3] *= -1
            for v2, v3 in v1:
                v4, v5 = (a2 + v2, a3 + v3)
                if not (0 <= v4 < len(a1) and 0 <= v5 < len(a1[0]) and (a1[v4][v5] > 0)):
                    continue
                v1 = max(v1, backtracking(a1, v4, v5))
            a1[a2][a3] *= -1
            return a1[a2][a3] + v1
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4]:
                    v2 = max(v2, backtracking(a1, v3, v4))
        return v2
