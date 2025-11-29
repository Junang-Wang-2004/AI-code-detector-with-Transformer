class C1(object):

    def __init__(self, a1, a2):
        self.__start = a1
        self.__end = a2
        self.__left = None
        self.__right = None

    def insert(self, a1):
        if a1.__start >= self.__end:
            if not self.__right:
                self.__right = a1
                return True
            return self.__right.insert(a1)
        elif a1.__end <= self.__start:
            if not self.__left:
                self.__left = a1
                return True
            return self.__left.insert(a1)
        else:
            return False

class C2(object):

    def __init__(self):
        self.__root = None

    def book(self, a1, a2):
        """
        """
        if self.__root is None:
            self.__root = C1(a1, a2)
            return True
        return self.root.insert(C1(a1, a2))
