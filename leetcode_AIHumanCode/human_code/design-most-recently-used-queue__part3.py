# Time:  ctor:  O(n)
# Space: fetch: O(sqrt(n))
import collections
import math


# sqrt decomposition solution
class MRUQueue3(object):

    def __init__(self, n):
        """
        """
        self.__buckets = [collections.deque() for _ in range(int(math.ceil(n**0.5)))]
        for i in range(n):
            self.__buckets[i//len(self.__buckets)].append(i+1)

    def fetch(self, k):
        """
        """
        k -= 1
        left, idx = divmod(k, len(self.__buckets))
        val = self.__buckets[left][idx]
        del self.__buckets[left][idx]
        self.__buckets[-1].append(val)
        for i in reversed(range(left, len(self.__buckets)-1)):
            x = self.__buckets[i+1].popleft()
            self.__buckets[i].append(x)
        return val
