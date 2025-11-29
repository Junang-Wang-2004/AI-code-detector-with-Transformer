import collections

class C1(object):

    def __init__(self):
        self.__q = collections.deque()

    def ping(self, a1):
        """
        """
        self.__q.append(a1)
        while self.__q[0] < a1 - 3000:
            self.__q.popleft()
        return len(self.__q)
