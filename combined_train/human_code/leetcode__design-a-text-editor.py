class C1(object):

    def __init__(self):
        self.__LAST_COUNT = 10
        self.__left = []
        self.__right = []

    def addText(self, a1):
        """
        """
        for v1 in a1:
            self.__left.append(v1)

    def deleteText(self, a1):
        """
        """
        return self.__move(a1, self.__left, None)

    def cursorLeft(self, a1):
        """
        """
        self.__move(a1, self.__left, self.__right)
        return self.__last_characters()

    def cursorRight(self, a1):
        """
        """
        self.__move(a1, self.__right, self.__left)
        return self.__last_characters()

    def __move(self, a1, a2, a3):
        v1 = min(a1, len(a2))
        for v2 in range(v1):
            if a3 is not None:
                a3.append(a2[-1])
            a2.pop()
        return v1

    def __last_characters(self):
        return ''.join(self.__left[-self.__LAST_COUNT:])
