# Time:  O(1)
# Space: O(w)

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.__size = size
        self.__sum = 0
        self.__q = deque()

    def next(self, val):
        """
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        return 1.0 * self.__sum / len(self.__q)



