import heapq

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__stks = []
        self.__c = a1
        self.__min_heap = []

    def push(self, a1):
        """
        """
        if self.__min_heap:
            v1 = heapq.heappop(self.__min_heap)
            if v1 < len(self.__stks):
                self.__stks[v1].append(a1)
                return
            self.__min_heap = []
        if not self.__stks or len(self.__stks[-1]) == self.__c:
            self.__stks.append([])
        self.__stks[-1].append(a1)

    def pop(self):
        """
        """
        while self.__stks and (not self.__stks[-1]):
            self.__stks.pop()
        if not self.__stks:
            return -1
        return self.__stks[-1].pop()

    def popAtStack(self, a1):
        """
        """
        if a1 >= len(self.__stks) or not self.__stks[a1]:
            return -1
        heapq.heappush(self.__min_heap, a1)
        return self.__stks[a1].pop()
