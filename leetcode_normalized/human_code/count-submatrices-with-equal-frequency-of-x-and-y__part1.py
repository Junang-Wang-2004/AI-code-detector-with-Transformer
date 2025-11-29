class C1(object):

    def numberOfSubmatrices(self, a1):
        """
        """
        v1 = 0
        v2 = [[0] * (len(a1[0]) + 1) for v3 in range(len(a1) + 1)]
        v4 = [[0] * (len(a1[0]) + 1) for v3 in range(len(a1) + 1)]
        for v5 in range(len(a1)):
            for v6 in range(len(a1[0])):
                v2[v5 + 1][v6 + 1] = v2[v5][v6 + 1] + v2[v5 + 1][v6] - v2[v5][v6] + int(a1[v5][v6] == 'X')
                v4[v5 + 1][v6 + 1] = v4[v5][v6 + 1] + v4[v5 + 1][v6] - v4[v5][v6] + int(a1[v5][v6] == 'Y')
                v1 += int(v2[v5 + 1][v6 + 1] == v4[v5 + 1][v6 + 1] != 0)
        return v1
