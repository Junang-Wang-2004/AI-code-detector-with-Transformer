class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__w = a1
        self.__h = a2
        self.__curr = 0

    def move(self, a1):
        """
        """
        self.__curr += a1

    def getPos(self):
        """
        """
        v1 = self.__curr % (2 * (self.__w - 1 + (self.__h - 1)))
        if v1 < self.__w:
            return [v1, 0]
        v1 -= self.__w - 1
        if v1 < self.__h:
            return [self.__w - 1, v1]
        v1 -= self.__h - 1
        if v1 < self.__w:
            return [self.__w - 1 - v1, self.__h - 1]
        v1 -= self.__w - 1
        return [0, self.__h - 1 - v1]

    def getDir(self):
        """
        """
        v1 = self.__curr % (2 * (self.__w - 1 + (self.__h - 1)))
        if v1 < self.__w:
            return 'South' if v1 == 0 and self.__curr else 'East'
        v1 -= self.__w - 1
        if v1 < self.__h:
            return 'North'
        v1 -= self.__h - 1
        if v1 < self.__w:
            return 'West'
        v1 -= self.__w - 1
        return 'South'
