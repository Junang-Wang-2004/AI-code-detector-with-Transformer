import itertools

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__it = itertools.combinations(a1, a2)
        self.__curr = None
        self.__last = a1[-a2:]

    def __next__(self):
        """
        """
        self.__curr = ''.join(next(self.__it))
        return self.__curr

    def hasNext(self):
        """
        """
        return self.__curr != self.__last
