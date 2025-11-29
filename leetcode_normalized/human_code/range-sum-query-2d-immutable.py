class C1(object):

    def __init__(self, a1):
        """
        initialize your data structure here.
        """
        if not a1:
            return
        v1, v2 = (len(a1), len(a1[0]))
        self.__sums = [[0 for v3 in range(v2 + 1)] for v3 in range(v1 + 1)]
        for v4 in range(1, v1 + 1):
            for v5 in range(1, v2 + 1):
                self.__sums[v4][v5] = self.__sums[v4][v5 - 1] + self.__sums[v4 - 1][v5] - self.__sums[v4 - 1][v5 - 1] + a1[v4 - 1][v5 - 1]

    def sumRegion(self, a1, a2, a3, a4):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        """
        return self.__sums[a3 + 1][a4 + 1] - self.__sums[a3 + 1][a2] - self.__sums[a1][a4 + 1] + self.__sums[a1][a2]
