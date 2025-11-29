class C1(object):

    def maxVacationDays(self, a1, a2):
        """
        """
        if not a2 or not a1:
            return 0
        v1 = [[0] * len(a2) for v2 in range(2)]
        for v3 in reversed(range(len(a2[0]))):
            for v4 in range(len(a2)):
                v1[v3 % 2][v4] = a2[v4][v3] + v1[(v3 + 1) % 2][v4]
                for v5 in range(len(a2)):
                    if a1[v4][v5] == 1:
                        v1[v3 % 2][v4] = max(v1[v3 % 2][v4], a2[v5][v3] + v1[(v3 + 1) % 2][v5])
        return v1[0][0]
