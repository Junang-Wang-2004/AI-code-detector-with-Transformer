class C1(object):

    def minPathCost(self, a1, a2):
        """
        """
        v1 = [[0] * len(a1[0]) for v2 in range(2)]
        v1[0] = [a1[0][j] for v3 in range(len(a1[0]))]
        for v4 in range(len(a1) - 1):
            for v3 in range(len(a1[0])):
                v1[(v4 + 1) % 2][v3] = min((v1[v4 % 2][k] + a2[x][v3] for v5, v6 in enumerate(a1[v4]))) + a1[v4 + 1][v3]
        return min(v1[(len(a1) - 1) % 2])
