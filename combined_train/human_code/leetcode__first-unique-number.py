import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__q = collections.OrderedDict()
        self.__dup = set()
        for v1 in a1:
            self.add(v1)

    def showFirstUnique(self):
        """
        """
        if self.__q:
            return next(iter(self.__q))
        return -1

    def add(self, a1):
        """
        """
        if a1 not in self.__dup and a1 not in self.__q:
            self.__q[a1] = None
            return
        if a1 in self.__q:
            self.__q.pop(a1)
            self.__dup.add(a1)
