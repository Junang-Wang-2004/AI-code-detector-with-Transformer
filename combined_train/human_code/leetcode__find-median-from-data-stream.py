from heapq import heappush, heappop

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__max_heap = []
        self.__min_heap = []

    def addNum(self, a1):
        """
        Adds a num into the data structure.
        """
        if not self.__max_heap or a1 > -self.__max_heap[0]:
            heappush(self.__min_heap, a1)
            if len(self.__min_heap) > len(self.__max_heap) + 1:
                heappush(self.__max_heap, -heappop(self.__min_heap))
        else:
            heappush(self.__max_heap, -a1)
            if len(self.__max_heap) > len(self.__min_heap):
                heappush(self.__min_heap, -heappop(self.__max_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        """
        return (-self.__max_heap[0] + self.__min_heap[0]) / 2.0 if len(self.__min_heap) == len(self.__max_heap) else self.__min_heap[0]
