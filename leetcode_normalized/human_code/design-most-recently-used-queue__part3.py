import collections
import math

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__buckets = [collections.deque() for v1 in range(int(math.ceil(a1 ** 0.5)))]
        for v2 in range(a1):
            self.__buckets[v2 // len(self.__buckets)].append(v2 + 1)

    def fetch(self, a1):
        """
        """
        a1 -= 1
        v2, v3 = divmod(a1, len(self.__buckets))
        v4 = self.__buckets[v2][v3]
        del self.__buckets[v2][v3]
        self.__buckets[-1].append(v4)
        for v5 in reversed(range(v2, len(self.__buckets) - 1)):
            v6 = self.__buckets[v5 + 1].popleft()
            self.__buckets[v5].append(v6)
        return v4
