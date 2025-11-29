import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__time = a1
        self.__lookup = collections.OrderedDict()

    def __evict(self, a1):
        while self.__lookup and next(iter(self.__lookup.values())) <= a1:
            self.__lookup.popitem(last=False)

    def generate(self, a1, a2):
        """
        """
        self.__evict(a2)
        self.__lookup[a1] = a2 + self.__time

    def renew(self, a1, a2):
        """
        """
        self.__evict(a2)
        if a1 not in self.__lookup:
            return
        del self.__lookup[a1]
        self.__lookup[a1] = a2 + self.__time

    def countUnexpiredTokens(self, a1):
        """
        """
        self.__evict(a1)
        return len(self.__lookup)
