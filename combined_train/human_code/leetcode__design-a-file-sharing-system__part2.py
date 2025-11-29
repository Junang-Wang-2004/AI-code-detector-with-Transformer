import collections
import heapq

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__users = []
        self.__lookup = set()
        self.__chunks = collections.defaultdict(set)
        self.__min_heap = []

    def join(self, a1):
        """
        """
        if self.__min_heap:
            v1 = heapq.heappop(self.__min_heap)
        else:
            v1 = len(self.__users) + 1
            self.__users.append(set())
        self.__users[v1 - 1] = set(a1)
        self.__lookup.add(v1)
        for v2 in a1:
            self.__chunks[v2].add(v1)
        return v1

    def leave(self, a1):
        """
        """
        if a1 not in self.__lookup:
            return
        for v1 in self.__users[a1 - 1]:
            self.__chunks[v1].remove(a1)
        self.__lookup.remove(a1)
        self.__users[a1 - 1] = []
        heapq.heappush(self.__min_heap, a1)

    def request(self, a1, a2):
        """
        """
        v1 = sorted(self.__chunks[a2])
        if not v1:
            return
        self.__users[a1 - 1].add(a2)
        self.__chunks[a2].add(a1)
        return v1
