class C1(object):

    def __init__(self, a1):
        """
        """
        self.__lookup = [False] * a1
        self.__flip = False
        self.__cnt = 0

    def fix(self, a1):
        """
        """
        if self.__lookup[a1] == self.__flip:
            self.__lookup[a1] = not self.__lookup[a1]
            self.__cnt += 1

    def unfix(self, a1):
        """
        """
        if self.__lookup[a1] != self.__flip:
            self.__lookup[a1] = not self.__lookup[a1]
            self.__cnt -= 1

    def flip(self):
        """
        """
        self.__flip = not self.__flip
        self.__cnt = len(self.__lookup) - self.__cnt

    def all(self):
        """
        """
        return self.__cnt == len(self.__lookup)

    def one(self):
        """
        """
        return self.__cnt >= 1

    def count(self):
        """
        """
        return self.__cnt

    def toString(self):
        """
        """
        v1 = [''] * len(self.__lookup)
        for v2, v3 in enumerate(self.__lookup):
            v1[v2] = '1' if v3 != self.__flip else '0'
        return ''.join(v1)
