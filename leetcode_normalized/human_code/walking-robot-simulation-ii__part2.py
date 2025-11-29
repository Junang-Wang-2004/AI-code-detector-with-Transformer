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
        return self.__getPosDir()[0]

    def getDir(self):
        """
        """
        return self.__getPosDir()[1]

    def __getPosDir(self):
        v1 = self.__curr % (2 * (self.__w - 1 + (self.__h - 1)))
        if v1 < self.__w:
            return [[v1, 0], 'South' if v1 == 0 and self.__curr else 'East']
        v1 -= self.__w - 1
        if v1 < self.__h:
            return [[self.__w - 1, v1], 'North']
        v1 -= self.__h - 1
        if v1 < self.__w:
            return [[self.__w - 1 - v1, self.__h - 1], 'West']
        v1 -= self.__w - 1
        return [[0, self.__h - 1 - v1], 'South']
