class C1(object):
    v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))
    v2 = ((1, 1), (1, -1), (-1, 1), (-1, -1))

    def __init__(self, a1):
        """
        """
        self.__grid = a1
        self.__lookup = [None] * (len(a1) * len(a1[0]))
        for v1 in range(len(a1)):
            for v2 in range(len(a1[0])):
                self.__lookup[a1[v1][v2]] = (v1, v2)

    def adjacentSum(self, a1):
        """
        """
        return self.__sum(a1, C1.ADJACENTS)

    def diagonalSum(self, a1):
        """
        """
        return self.__sum(a1, C1.DIAGONALS)

    def __sum(self, a1, a2):
        v1, v2 = self.__lookup[a1]
        v3 = 0
        for v4, v5 in a2:
            v6, v7 = (v1 + v4, v2 + v5)
            if not (0 <= v6 < len(self.__grid) and 0 <= v7 < len(self.__grid[0])):
                continue
            v3 += self.__grid[v6][v7]
        return v3
