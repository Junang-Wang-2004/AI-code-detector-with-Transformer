from collections import deque

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__k = 300
        self.__dq = deque()
        self.__count = 0

    def hit(self, a1):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.getHits(a1)
        if self.__dq and self.__dq[-1][0] == a1:
            self.__dq[-1][1] += 1
        else:
            self.__dq.append([a1, 1])
        self.__count += 1

    def getHits(self, a1):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.__dq and self.__dq[0][0] <= a1 - self.__k:
            self.__count -= self.__dq.popleft()[1]
        return self.__count
