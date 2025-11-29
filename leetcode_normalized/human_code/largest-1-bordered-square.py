class C1(object):

    def largest1BorderedSquare(self, a1):
        """
        """
        v1, v2 = ([a[:] for v3 in a1], [v3[:] for v3 in a1])
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                if not a1[v4][v5]:
                    continue
                if v4:
                    v1[v4][v5] = v1[v4 - 1][v5] + 1
                if v5:
                    v2[v4][v5] = v2[v4][v5 - 1] + 1
        for v6 in reversed(range(1, min(len(a1), len(a1[0])) + 1)):
            for v4 in range(len(a1) - v6 + 1):
                for v5 in range(len(a1[0]) - v6 + 1):
                    if min(v1[v4 + v6 - 1][v5], v1[v4 + v6 - 1][v5 + v6 - 1], v2[v4][v5 + v6 - 1], v2[v4 + v6 - 1][v5 + v6 - 1]) >= v6:
                        return v6 * v6
        return 0
