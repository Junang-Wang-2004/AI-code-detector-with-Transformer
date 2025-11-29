import heapq

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__min_heap = list(range(1, a1 + 1))

    def reserve(self):
        """
        """
        return heapq.heappop(self.__min_heap)

    def unreserve(self, a1):
        """
        """
        heapq.heappush(self.__min_heap, a1)
