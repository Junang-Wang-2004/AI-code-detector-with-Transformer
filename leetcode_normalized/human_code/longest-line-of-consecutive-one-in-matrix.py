class C1(object):

    def longestLine(self, a1):
        """
        """
        if not a1:
            return 0
        v1 = 0
        v2 = [[[0] * 4 for v3 in range(len(a1[0]))] for v3 in range(2)]
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v2[v4 % 2][v5][:] = [0] * 4
                if a1[v4][v5] == 1:
                    v2[v4 % 2][v5][0] = v2[v4 % 2][v5 - 1][0] + 1 if v5 > 0 else 1
                    v2[v4 % 2][v5][1] = v2[(v4 - 1) % 2][v5][1] + 1 if v4 > 0 else 1
                    v2[v4 % 2][v5][2] = v2[(v4 - 1) % 2][v5 - 1][2] + 1 if v4 > 0 and v5 > 0 else 1
                    v2[v4 % 2][v5][3] = v2[(v4 - 1) % 2][v5 + 1][3] + 1 if v4 > 0 and v5 < len(a1[0]) - 1 else 1
                    v1 = max(v1, max(v2[v4 % 2][v5]))
        return v1
