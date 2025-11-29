# Time:  ctor:          O(1)
#        setCell:       O(logn)
#        unsetCell:     O(logn)
#        largestMatrix: O(logn) on average
# Space: O(n^3)
import collections
import heapq


# heap
class Matrix3D_2(object):

    def __init__(self, n):
        """
        """
        self.__matrix = {}
        self.__cnt = collections.defaultdict(int)
        self.__max_heap = [(0, -(n-1))]

    def setCell(self, x, y, z):
        """
        """
        if (x, y, z) in self.__matrix:
            return
        self.__matrix[x, y, z] = 1
        self.__cnt[x] += 1
        heapq.heappush(self.__max_heap, (-self.__cnt[x], -x))

    def unsetCell(self, x, y, z):
        """
        """
        if (x, y, z) not in self.__matrix:
            return
        del self.__matrix[x, y, z]
        self.__cnt[x] -= 1
        heapq.heappush(self.__max_heap, (-self.__cnt[x], -x))

    def largestMatrix(self):
        """
        """
        while self.__max_heap and -self.__max_heap[0][0] != self.__cnt[-self.__max_heap[0][1]]:
            heapq.heappop(self.__max_heap)
        return -self.__max_heap[0][1]
