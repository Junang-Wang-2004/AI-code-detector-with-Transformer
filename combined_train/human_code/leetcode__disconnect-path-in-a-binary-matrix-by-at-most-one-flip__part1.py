class C1(object):

    def isPossibleToCutPath(self, a1):
        """
        """
        for v1 in range(len(a1)):
            for v2 in range(len(a1[0])):
                if (v1, v2) == (0, 0) or a1[v1][v2] == 0:
                    continue
                if (v1 - 1 < 0 or a1[v1 - 1][v2] == 0) and (v2 - 1 < 0 or a1[v1][v2 - 1] == 0):
                    a1[v1][v2] = 0
        for v1 in reversed(range(len(a1))):
            for v2 in reversed(range(len(a1[0]))):
                if (v1, v2) == (len(a1) - 1, len(a1[0]) - 1) or a1[v1][v2] == 0:
                    continue
                if (v1 + 1 >= len(a1) or a1[v1 + 1][v2] == 0) and (v2 + 1 >= len(a1[0]) or a1[v1][v2 + 1] == 0):
                    a1[v1][v2] = 0
        v3 = [0] * (len(a1) + len(a1[0]) - 1)
        for v1 in range(len(a1)):
            for v2 in range(len(a1[0])):
                v3[v1 + v2] += a1[v1][v2]
        return any((v3[v1] <= 1 for v1 in range(1, len(a1) + len(a1[0]) - 2)))
