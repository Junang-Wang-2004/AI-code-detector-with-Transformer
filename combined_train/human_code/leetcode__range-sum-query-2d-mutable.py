class C1(object):

    def __init__(self, a1):
        """
        initialize your data structure here.
        """
        if not a1:
            return
        self.__matrix = a1
        self.__bit = [[0] * (len(self.__matrix[0]) + 1) for v1 in range(len(self.__matrix) + 1)]
        for v2 in range(1, len(self.__bit)):
            for v3 in range(1, len(self.__bit[0])):
                self.__bit[v2][v3] = a1[v2 - 1][v3 - 1] + self.__bit[v2 - 1][v3] + self.__bit[v2][v3 - 1] - self.__bit[v2 - 1][v3 - 1]
        for v2 in reversed(range(1, len(self.__bit))):
            for v3 in reversed(range(1, len(self.__bit[0]))):
                v4, v5 = (v2 - (v2 & -v2), v3 - (v3 & -v3))
                self.__bit[v2][v3] = self.__bit[v2][v3] - self.__bit[v2][v5] - self.__bit[v4][v3] + self.__bit[v4][v5]

    def update(self, a1, a2, a3):
        """
        update the element at matrix[row,col] to val.
        """
        if a3 - self.__matrix[a1][a2]:
            self.__add(a1, a2, a3 - self.__matrix[a1][a2])
            self.__matrix[a1][a2] = a3

    def sumRegion(self, a1, a2, a3, a4):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        """
        return self.__sum(a3, a4) - self.__sum(a3, a2 - 1) - self.__sum(a1 - 1, a4) + self.__sum(a1 - 1, a2 - 1)

    def __sum(self, a1, a2):
        a1 += 1
        a2 += 1
        v3 = 0
        v4 = a1
        while v4 > 0:
            v5 = a2
            while v5 > 0:
                v3 += self.__bit[v4][v5]
                v5 -= v5 & -v5
            v4 -= v4 & -v4
        return v3

    def __add(self, a1, a2, a3):
        a1 += 1
        a2 += 1
        v3 = a1
        while v3 <= len(self.__matrix):
            v4 = a2
            while v4 <= len(self.__matrix[0]):
                self.__bit[v3][v4] += a3
                v4 += v4 & -v4
            v3 += v3 & -v3
