import random

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__n = a1 - len(a2)
        a2.sort()
        self.__blacklist = a2

    def pick(self):
        """
        """
        v1 = random.randint(0, self.__n - 1)
        v2, v3 = (0, len(self.__blacklist) - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if v1 + v4 < self.__blacklist[v4]:
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v1 + v2
