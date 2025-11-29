import heapq

class C1(object):

    def __init__(self):
        self.__curr = 0
        self.__lookup = {}
        self.__min_heap = []
        self.__max_heap = []

    def update(self, a1, a2):
        """
        """

        def full_delete(a1, a2):
            a1[:] = [x for v1 in set(a1) if a2 * v1[0] == self.__lookup[v1[1]]]
            heapq.heapify(a1)
        if a1 > self.__curr:
            self.__curr = a1
        self.__lookup[a1] = a2
        heapq.heappush(self.__min_heap, (a2, a1))
        heapq.heappush(self.__max_heap, (-a2, a1))
        if len(self.__min_heap) > 2 * len(self.__lookup):
            full_delete(self.__min_heap, 1)
            full_delete(self.__max_heap, -1)

    def current(self):
        """
        """
        return self.__lookup[self.__curr]

    def maximum(self):
        """
        """
        while self.__max_heap and self.__lookup[self.__max_heap[0][1]] != -self.__max_heap[0][0]:
            heapq.heappop(self.__max_heap)
        return -self.__max_heap[0][0]

    def minimum(self):
        """
        """
        while self.__min_heap and self.__lookup[self.__min_heap[0][1]] != self.__min_heap[0][0]:
            heapq.heappop(self.__min_heap)
        return self.__min_heap[0][0]
