import collections
from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__m = a1
        self.__k = a2
        self.__dq = collections.deque()
        self.__sl = SortedList()
        self.__total = self.__first_k = self.__last_k = 0

    def addElement(self, a1):
        """
        """
        if len(self.__dq) == self.__m:
            self.__remove(self.__dq.popleft())
        self.__dq.append(a1)
        self.__add(a1)

    def calculateMKAverage(self):
        """
        """
        if len(self.__sl) < self.__m:
            return -1
        return (self.__total - self.__first_k - self.__last_k) // (self.__m - 2 * self.__k)

    def __add(self, a1):
        self.__total += a1
        v1 = self.__sl.bisect_left(a1)
        if v1 < self.__k:
            self.__first_k += a1
            if len(self.__sl) >= self.__k:
                self.__first_k -= self.__sl[self.__k - 1]
        if v1 > len(self.__sl) - self.__k:
            self.__last_k += a1
            if len(self.__sl) >= self.__k:
                self.__last_k -= self.__sl[-self.__k]
        self.__sl.add(a1)

    def __remove(self, a1):
        self.__total -= a1
        v1 = self.__sl.index(a1)
        if v1 < self.__k:
            self.__first_k -= a1
            self.__first_k += self.__sl[self.__k]
        elif v1 > len(self.__sl) - 1 - self.__k:
            self.__last_k -= a1
            self.__last_k += self.__sl[-1 - self.__k]
        self.__sl.remove(a1)
