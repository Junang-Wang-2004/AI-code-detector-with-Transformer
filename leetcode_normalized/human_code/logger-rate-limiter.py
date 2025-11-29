import collections

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dq = collections.deque()
        self.__printed = set()

    def shouldPrintMessage(self, a1, a2):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false. The timestamp is in seconds granularity.
        """
        while self.__dq and self.__dq[0][0] <= a1 - 10:
            self.__printed.remove(self.__dq.popleft()[1])
        if a2 in self.__printed:
            return False
        self.__dq.append((a1, a2))
        self.__printed.add(a2)
        return True
