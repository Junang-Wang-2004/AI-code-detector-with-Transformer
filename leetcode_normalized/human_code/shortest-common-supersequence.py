class C1(object):

    def shortestCommonSupersequence(self, a1, a2):
        """
        """
        v1 = [[0 for v2 in range(len(a2) + 1)] for v2 in range(2)]
        v3 = [[None for v2 in range(len(a2) + 1)] for v2 in range(len(a1) + 1)]
        for v4, v5 in enumerate(a1):
            v3[v4 + 1][0] = (v4, 0, v5)
        for v6, v5 in enumerate(a2):
            v3[0][v6 + 1] = (0, v6, v5)
        for v4 in range(len(a1)):
            for v6 in range(len(a2)):
                if v1[v4 % 2][v6 + 1] > v1[(v4 + 1) % 2][v6]:
                    v1[(v4 + 1) % 2][v6 + 1] = v1[v4 % 2][v6 + 1]
                    v3[v4 + 1][v6 + 1] = (v4, v6 + 1, a1[v4])
                else:
                    v1[(v4 + 1) % 2][v6 + 1] = v1[(v4 + 1) % 2][v6]
                    v3[v4 + 1][v6 + 1] = (v4 + 1, v6, a2[v6])
                if a1[v4] != a2[v6]:
                    continue
                if v1[v4 % 2][v6] + 1 > v1[(v4 + 1) % 2][v6 + 1]:
                    v1[(v4 + 1) % 2][v6 + 1] = v1[v4 % 2][v6] + 1
                    v3[v4 + 1][v6 + 1] = (v4, v6, a1[v4])
        v4, v6 = (len(a1), len(a2))
        v7 = []
        while v4 != 0 or v6 != 0:
            v4, v6, v5 = v3[v4][v6]
            v7.append(v5)
        v7.reverse()
        return ''.join(v7)
