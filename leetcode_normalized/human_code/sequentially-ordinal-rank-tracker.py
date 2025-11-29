from sortedcontainers import SortedList

class C1(object):

    def __init__(self):
        self.__sl = SortedList()
        self.__i = 0

    def add(self, a1, a2):
        """
        """
        self.__sl.add((-a2, a1))

    def get(self):
        """
        """
        self.__i += 1
        return self.__sl[self.__i - 1][1]
