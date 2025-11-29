import collections
from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__n = a1
        self.__matrix = set()
        self.__cnt = collections.defaultdict(int)
        self.__sl = SortedList([0])
        self.__lookup = collections.defaultdict(SortedList)
        self.__lookup[0].add(a1 - 1)

    def setCell(self, a1, a2, a3):
        """
        """
        if (a1, a2, a3) in self.__matrix:
            return
        self.__matrix.add((a1, a2, a3))
        if self.__cnt[a1] or a1 == self.__n - 1:
            self.__lookup[self.__cnt[a1]].remove(a1)
            if not self.__lookup[self.__cnt[a1]]:
                del self.__lookup[self.__cnt[a1]]
                self.__sl.remove(self.__cnt[a1])
        self.__cnt[a1] += 1
        if self.__cnt[a1] not in self.__lookup:
            self.__sl.add(self.__cnt[a1])
        self.__lookup[self.__cnt[a1]].add(a1)

    def unsetCell(self, a1, a2, a3):
        """
        """
        if (a1, a2, a3) not in self.__matrix:
            return
        self.__matrix.remove((a1, a2, a3))
        self.__lookup[self.__cnt[a1]].remove(a1)
        if not self.__lookup[self.__cnt[a1]]:
            del self.__lookup[self.__cnt[a1]]
            self.__sl.remove(self.__cnt[a1])
        self.__cnt[a1] -= 1
        if self.__cnt[a1] or a1 == self.__n - 1:
            if self.__cnt[a1] not in self.__lookup:
                self.__sl.add(self.__cnt[a1])
            self.__lookup[self.__cnt[a1]].add(a1)

    def largestMatrix(self):
        """
        """
        return self.__lookup[self.__sl[-1]][-1]
