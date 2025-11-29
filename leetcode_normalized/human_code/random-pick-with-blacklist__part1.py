import random

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__n = a1 - len(a2)
        self.__lookup = {}
        v1 = iter(set(range(self.__n, a1)) - set(a2))
        for v2 in a2:
            if v2 < self.__n:
                self.__lookup[v2] = next(v1)

    def pick(self):
        """
        """
        v1 = random.randint(0, self.__n - 1)
        return self.__lookup[v1] if v1 in self.__lookup else v1
