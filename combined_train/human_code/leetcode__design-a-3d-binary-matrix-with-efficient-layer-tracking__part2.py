import collections
import heapq

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__matrix = {}
        self.__cnt = collections.defaultdict(int)
        self.__max_heap = [(0, -(a1 - 1))]

    def setCell(self, a1, a2, a3):
        """
        """
        if (a1, a2, a3) in self.__matrix:
            return
        self.__matrix[a1, a2, a3] = 1
        self.__cnt[a1] += 1
        heapq.heappush(self.__max_heap, (-self.__cnt[a1], -a1))

    def unsetCell(self, a1, a2, a3):
        """
        """
        if (a1, a2, a3) not in self.__matrix:
            return
        del self.__matrix[a1, a2, a3]
        self.__cnt[a1] -= 1
        heapq.heappush(self.__max_heap, (-self.__cnt[a1], -a1))

    def largestMatrix(self):
        """
        """
        while self.__max_heap and -self.__max_heap[0][0] != self.__cnt[-self.__max_heap[0][1]]:
            heapq.heappop(self.__max_heap)
        return -self.__max_heap[0][1]
