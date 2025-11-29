from collections import deque

class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here.
        """
        self.__size = a1
        self.__sum = 0
        self.__q = deque()

    def next(self, a1):
        """
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += a1
        self.__q.append(a1)
        return 1.0 * self.__sum / len(self.__q)
