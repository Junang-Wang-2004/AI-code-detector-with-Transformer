# Time:  ctor:          O(1)
#        setCell:       O(logn)
#        unsetCell:     O(logn)
#        largestMatrix: O(logn)
# Space: O(n^3)

import collections
from sortedcontainers import SortedList


# sorted list
class Matrix3D(object):

    def __init__(self, n):
        """
        """
        self.__n = n
        self.__matrix = set()
        self.__cnt = collections.defaultdict(int)
        self.__sl = SortedList([0])
        self.__lookup = collections.defaultdict(SortedList)
        self.__lookup[0].add(n-1)

    def setCell(self, x, y, z):
        """
        """
        if (x, y, z) in self.__matrix:
            return
        self.__matrix.add((x, y, z))
        if self.__cnt[x] or x == self.__n-1:
            self.__lookup[self.__cnt[x]].remove(x)
            if not self.__lookup[self.__cnt[x]]:
                del self.__lookup[self.__cnt[x]]
                self.__sl.remove(self.__cnt[x])
        self.__cnt[x] += 1
        if self.__cnt[x] not in self.__lookup:
            self.__sl.add(self.__cnt[x])
        self.__lookup[self.__cnt[x]].add(x)

    def unsetCell(self, x, y, z):
        """
        """
        if (x, y, z) not in self.__matrix:
            return
        self.__matrix.remove((x, y, z))
        self.__lookup[self.__cnt[x]].remove(x)
        if not self.__lookup[self.__cnt[x]]:
            del self.__lookup[self.__cnt[x]]
            self.__sl.remove(self.__cnt[x])
        self.__cnt[x] -= 1
        if self.__cnt[x] or x == self.__n-1:
            if self.__cnt[x] not in self.__lookup:
                self.__sl.add(self.__cnt[x])
            self.__lookup[self.__cnt[x]].add(x)

    def largestMatrix(self):
        """
        """
        return self.__lookup[self.__sl[-1]][-1]        


