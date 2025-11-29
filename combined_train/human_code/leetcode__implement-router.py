import collections
from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__size = a1
        self.__q = collections.deque()
        self.__lookup = collections.defaultdict(SortedList)

    def addPacket(self, a1, a2, a3):
        """
        """
        if (a3, a1) in self.__lookup[a2]:
            return False
        self.__lookup[a2].add((a3, a1))
        if len(self.__q) == self.__size:
            v1, v2, v3 = self.__q.popleft()
            self.__lookup[v2].remove((v3, v1))
        self.__q.append((a1, a2, a3))
        return True

    def forwardPacket(self):
        """
        """
        if not self.__q:
            return []
        v1, v2, v3 = self.__q.popleft()
        self.__lookup[v2].remove((v3, v1))
        return [v1, v2, v3]

    def getCount(self, a1, a2, a3):
        """
        """
        return self.__lookup[a1].bisect_left((a3 + 1, 0)) - self.__lookup[a1].bisect_left((a2, 0))
