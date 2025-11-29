import random

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__n_rows = a1
        self.__n_cols = a2
        self.__n = a1 * a2
        self.__lookup = {}

    def flip(self):
        """
        """
        self.__n -= 1
        v1 = random.randint(0, self.__n)
        v2 = self.__lookup.get(v1, v1)
        self.__lookup[v1] = self.__lookup.get(self.__n, self.__n)
        return divmod(v2, self.__n_cols)

    def reset(self):
        """
        """
        self.__n = self.__n_rows * self.__n_cols
        self.__lookup = {}
