class C1(object):

    def checkValidGrid(self, a1):
        """
        """
        v1 = {a1[i][j]: (i, j) for v2 in range(len(a1)) for v3 in range(len(a1[0]))}
        return a1[0][0] == 0 and all((sorted([abs(v1[v2 + 1][0] - v1[v2][0]), abs(v1[v2 + 1][1] - v1[v2][1])]) == [1, 2] for v2 in range(len(v1) - 1)))
