import heapq

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__num = a1
        self.__seats = {-1: [-1, self.__num], self.__num: [-1, self.__num]}
        self.__max_heap = [(-self.__distance((-1, self.__num)), -1, self.__num)]

    def seat(self):
        """
        """
        while self.__max_heap[0][1] not in self.__seats or self.__max_heap[0][2] not in self.__seats or self.__seats[self.__max_heap[0][1]][1] != self.__max_heap[0][2] or (self.__seats[self.__max_heap[0][2]][0] != self.__max_heap[0][1]):
            heapq.heappop(self.__max_heap)
        v1, v2, v3 = heapq.heappop(self.__max_heap)
        v4 = 0 if v2 == -1 else self.__num - 1 if v3 == self.__num else (v2 + v3) // 2
        self.__seats[v4] = [v2, v3]
        heapq.heappush(self.__max_heap, (-self.__distance((v2, v4)), v2, v4))
        heapq.heappush(self.__max_heap, (-self.__distance((v4, v3)), v4, v3))
        self.__seats[v2][1] = v4
        self.__seats[v3][0] = v4
        return v4

    def leave(self, a1):
        """
        """
        v1, v2 = self.__seats[a1]
        self.__seats.pop(a1)
        self.__seats[v1][1] = v2
        self.__seats[v2][0] = v1
        heapq.heappush(self.__max_heap, (-self.__distance((v1, v2)), v1, v2))

    def __distance(self, a1):
        return a1[1] - a1[0] - 1 if a1[0] == -1 or a1[1] == self.__num else (a1[1] - a1[0]) // 2
