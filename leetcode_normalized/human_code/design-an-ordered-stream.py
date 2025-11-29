class C1(object):

    def __init__(self, a1):
        """
        """
        self.__i = 0
        self.__values = [None] * a1

    def insert(self, a1, a2):
        """
        """
        a1 -= 1
        self.__values[a1] = a2
        v2 = []
        if self.__i != a1:
            return v2
        while self.__i < len(self.__values) and self.__values[self.__i]:
            v2.append(self.__values[self.__i])
            self.__i += 1
        return v2
