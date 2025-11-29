class C1(object):

    def maxMoves(self, a1):
        """
        """
        v1 = set(range(len(a1)))
        for v2 in range(len(a1[0]) - 1):
            v3 = set()
            for v4 in v1:
                if a1[v4][v2] < a1[v4][v2 + 1]:
                    v3.add(v4)
                if v4 - 1 >= 0 and a1[v4][v2] < a1[v4 - 1][v2 + 1]:
                    v3.add(v4 - 1)
                if v4 + 1 < len(a1) and a1[v4][v2] < a1[v4 + 1][v2 + 1]:
                    v3.add(v4 + 1)
            v1 = v3
            if not v1:
                break
        else:
            v2 = len(a1[0]) - 1
        return v2
