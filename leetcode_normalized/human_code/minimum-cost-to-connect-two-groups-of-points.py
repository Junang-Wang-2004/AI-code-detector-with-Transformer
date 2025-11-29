class C1(object):

    def connectTwoGroups(self, a1):
        """
        """
        v1 = 2 ** len(a1[0])
        v2 = [[float('inf')] * v1 for v3 in range(2)]
        v2[0][0] = 0
        for v4 in range(len(a1)):
            v2[(v4 + 1) % 2] = [float('inf')] * v1
            for v5 in range(v1):
                v6 = 1
                for v7 in range(len(a1[0])):
                    v2[v4 % 2][v5 | v6] = min(v2[v4 % 2][v5 | v6], a1[v4][v7] + v2[v4 % 2][v5])
                    v2[(v4 + 1) % 2][v5 | v6] = min(v2[(v4 + 1) % 2][v5 | v6], a1[v4][v7] + v2[v4 % 2][v5])
                    v6 <<= 1
        return v2[len(a1) % 2][-1]
