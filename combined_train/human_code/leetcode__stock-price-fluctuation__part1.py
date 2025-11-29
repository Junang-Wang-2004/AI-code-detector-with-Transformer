from sortedcontainers import SortedList

class C1(object):

    def __init__(self):
        self.__curr = 0
        self.__lookup = {}
        self.__sl_by_price = SortedList()

    def update(self, a1, a2):
        """
        """
        if a1 > self.__curr:
            self.__curr = a1
        if a1 in self.__lookup:
            self.__sl_by_price.remove(self.__lookup[a1])
        self.__lookup[a1] = a2
        self.__sl_by_price.add(a2)

    def current(self):
        """
        """
        return self.__lookup[self.__curr]

    def maximum(self):
        """
        """
        return next(reversed(self.__sl_by_price))

    def minimum(self):
        """
        """
        return next(iter(self.__sl_by_price))
