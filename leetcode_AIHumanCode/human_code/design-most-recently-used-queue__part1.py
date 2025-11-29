# Time:  ctor:  O(nlogn)
# Space: fetch: O(logn)

from sortedcontainers import SortedList


# balanced bst solution
class MRUQueue(object):

    def __init__(self, n):
        """
        """
        self.__sl = SortedList((i-1, i) for i in range(1, n+1))  

    def fetch(self, k):
        """
        """
        last, _ = self.__sl[-1]
        _, val = self.__sl.pop(k-1)
        self.__sl.add((last+1, val))
        return val


