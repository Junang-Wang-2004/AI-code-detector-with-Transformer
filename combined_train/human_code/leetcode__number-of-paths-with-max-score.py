class C1(object):

    def pathsWithMaxScore(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[1, 0], [0, 1], [1, 1]]
        v3 = [[[0, 0] for v4 in range(len(a1[0]) + 1)] for v4 in range(2)]
        v3[(len(a1) - 1) % 2][len(a1[0]) - 1] = [0, 1]
        for v4 in reversed(range(len(a1))):
            for v5 in reversed(range(len(a1[0]))):
                if a1[v4][v5] in 'XS':
                    continue
                v3[v4 % 2][v5] = [0, 0]
                for v6, v7 in v2:
                    if v3[v4 % 2][v5][0] < v3[(v4 + v6) % 2][v5 + v7][0]:
                        v3[v4 % 2][v5] = v3[(v4 + v6) % 2][v5 + v7][:]
                    elif v3[v4 % 2][v5][0] == v3[(v4 + v6) % 2][v5 + v7][0]:
                        v3[v4 % 2][v5][1] = (v3[v4 % 2][v5][1] + v3[(v4 + v6) % 2][v5 + v7][1]) % v1
                if v3[v4 % 2][v5][1] and a1[v4][v5] != 'E':
                    v3[v4 % 2][v5][0] += int(a1[v4][v5])
        return v3[0][0]
