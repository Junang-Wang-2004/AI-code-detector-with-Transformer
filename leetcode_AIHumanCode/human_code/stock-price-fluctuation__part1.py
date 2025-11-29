# Time:  ctor:    O(1)
#        update:  O(logn)
#        current: O(1)
#        max:     O(1)
#        min:     O(1)
# Space: O(n)

from sortedcontainers import SortedList


class StockPrice(object):

    def __init__(self):
        self.__curr = 0
        self.__lookup = {}
        self.__sl_by_price = SortedList()

    def update(self, timestamp, price):
        """
        """
        if timestamp > self.__curr:
            self.__curr = timestamp
        if timestamp in self.__lookup:
            self.__sl_by_price.remove(self.__lookup[timestamp])
        self.__lookup[timestamp] = price
        self.__sl_by_price.add(price)

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


