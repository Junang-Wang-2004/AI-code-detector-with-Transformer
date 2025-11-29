import heapq

class C1(object):

    def __init__(self):
        self.__n = 1
        self.__lookup = set()
        self.__min_heap = []

    def popSmallest(self):
        """
        """
        if self.__min_heap:
            v1 = heapq.heappop(self.__min_heap)
            self.__lookup.remove(v1)
            return v1
        v1 = self.__n
        self.__n += 1
        return v1

    def addBack(self, a1):
        """
        """
        if a1 >= self.__n or a1 in self.__lookup:
            return
        self.__lookup.add(a1)
        heapq.heappush(self.__min_heap, a1)
