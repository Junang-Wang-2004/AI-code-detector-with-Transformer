from random import randint
import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__lookup = collections.defaultdict(list)
        for v1, v2 in enumerate(a1):
            self.__lookup[v2].append(v1)

    def pick(self, a1):
        """
        """
        return self.__lookup[a1][randint(0, len(self.__lookup[a1]) - 1)]
