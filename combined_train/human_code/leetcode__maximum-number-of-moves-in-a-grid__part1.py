class C1(object):

    def maxMoves(self, a1):
        """
        """
        v1 = [True] * len(a1)
        v2 = 0
        for v3 in range(len(a1[0]) - 1):
            v4 = [False] * len(a1)
            for v5 in range(len(a1)):
                if not v1[v5]:
                    continue
                if a1[v5][v3] < a1[v5][v3 + 1]:
                    v4[v5] = True
                if v5 - 1 >= 0 and a1[v5][v3] < a1[v5 - 1][v3 + 1]:
                    v4[v5 - 1] = True
                if v5 + 1 < len(a1) and a1[v5][v3] < a1[v5 + 1][v3 + 1]:
                    v4[v5 + 1] = True
            v1 = v4
            if not sum(v1):
                break
        else:
            v3 = len(a1[0]) - 1
        return v3
