import heapq

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__k = a1
        self.__min_heap = []
        for v1 in a2:
            self.add(v1)

    def add(self, a1):
        """
        """
        heapq.heappush(self.__min_heap, a1)
        if len(self.__min_heap) > self.__k:
            heapq.heappop(self.__min_heap)
        return self.__min_heap[0]
